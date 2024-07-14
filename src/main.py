#!/usr/bin/env python3

# * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# * POSSIBILITY OF SUCH DAMAGE.

import csv
import os
import numpy as np
import networkx as nx
import subprocess
import json
import sys

# Generate adjacency list for block (one block per file)
def generate_ddg_fingerprint(ddg_size):
  directory = os.path.join(os.getcwd(), "/ddg/tmp/ddg_segments")

  i = 0

  hashes = {}
  d = os.path.join(directory, dirname)
  for filename in os.listdir(d):
    f = os.path.join(d, filename)
    # checking if it is a file
    if os.path.isfile(f):
      with open(f, "r") as myfile:
        ddg = np.zeros([ddg_size, ddg_size])

        # create a dictionary of operands' indices in the DDG
        operand_index_dictionary = {}

        # look at every line in file
        for line in myfile:
          # split into opcode and operands
          tokens = line.split('\t')

          operands = ""

          if len(tokens) > 1:
            operands = tokens[1]

          operand_tokens = operands.split(',')

          if len(operand_tokens) > 1:
            dest = get_index_for_operand(operand_tokens[0], operand_index_dictionary)
            source = get_index_for_operand(operand_tokens[1], operand_index_dictionary)

            # add an edge to DDG matrix
            ddg[dest][source] = 1
            ddg[source][dest] = 1

        G = nx.from_numpy_array(ddg)
        G.remove_nodes_from(list(nx.isolates(G)))
        degree_sequence = sorted((d for n, d in G.degree()), reverse=True)

        hashes[str(nx.weisfeiler_lehman_graph_hash(G))] = 1

    i += 1
    print(f"  {i}/{len(file_list)} : {(i/len(file_list)*100):.0f}% complete")

    # save hashes to a file

    ddg_dir = os.path.join(os.getcwd(), "/tmp/ddg_fingerprints/")
    f = open(ddg_dir + dirname + ".csv", "w")
    for k in hashes.keys():
      f.write(str(k))
      f.write(",\n")
    f.close()


# extract DDG's, put in adjacency list
def get_index_for_operand(token, operand_index_dictionary):
  # check for indirection in source and destination operands
  if '+' in token:
    # get key from register indirect token
    key_tokens = token.split(' ')
    key = key_tokens[1] + '_' + key_tokens[3]

    # is the operand a key in the dictionary? if so, get the index
    if key in operand_index_dictionary.keys():
      return operand_index_dictionary[key]
    
  else:
    # does not have indirection
    # is the operand a key in the dictionary? if so, get the index
    if token in operand_index_dictionary.keys():
      return operand_index_dictionary[token]

    key = token
      
  # key doesn't exist, add it to the dictionary
  index = len(operand_index_dictionary.keys()) + 1
  operand_index_dictionary[key] = index

  return index


# run objdump, decompile binaries, segment source file into 
# basic blocks, generates hundreds of files
def init(filepath):
  ddg_size = 1000
  filename = os.path.basename(filepath)
  
  with open("/tmp/ddg/asm/" + filename + "_src", "w") as myfile:
    ps1 = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", "--x86-asm-syntax=intel", filepath], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    ps2 = subprocess.Popen(["cut", "-f2-6"], stdin=ps1.stdout, stdout=myfile, stderr=subprocess.DEVNULL)
    subprocess.Popen(["mkdir", "-p", "/tmp/ddg/blocks/" + filename])

  f = os.path.join(os.getcwd(), "/tmp/ddg/asm/", filename + "_src")

  perl_command = f'perl -ne \'print $_; open STDOUT, ">", "/tmp/ddg/blocks/{filename}/" . ++$n if /jmp/ || /jg/ || /jge/ || /je/ || /jl/ || /jne/ || /jl/\' {f}'
  ps1 = subprocess.Popen(perl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, error = ps1.communicate()

  generate_ddg_fingerprint(ddg_size)


def help():
  print("ddg - Data dependency graph extraction tool.")
  print("\nusage: ddg <source> [<args>]")
  print("    source - path to binary to extract data dependencies")
  print("\nOptional parameters:")
  print("    dest - path for output file, defaults to current directory ")
  print("    DDG_SIZE - configures the size of the binary's data\n      dependency graphs, defaults to 1000")
  print("\nauthor: John Musgrave <@musgravejw>, 2019-2022.\n")


if __name__ == "__main__":
  if len(sys.argv) == 1:
    help()
  else:
    init(sys.argv[1])
