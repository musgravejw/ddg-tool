# ddg-tool
![GitHub License](https://img.shields.io/github/license/musgravejw/ddg-tool)
![GitHub Tag](https://img.shields.io/github/v/tag/musgravejw/ddg-tool)

This tool extracts a set of data dependency graphs from a static binary.  The binary's source is segmented based on the program's control flow graph into basic block segments.  For each basic block segment, the data dependency graph is extracted for data movement and arithmetic instructions.  This set of graphs can be exported in a hash of isomorphic uniqueness ~~or the raw graphs can be exported in an adjacency list format~~.

# Citation
To cite this tool, please use the following BibTex citation:
```
@INPROCEEDINGS{10670673,
  author={Musgrave, John and Ralescu, Anca},
  booktitle={NAECON 2024 - IEEE National Aerospace and Electronics Conference}, 
  title={kNN Classification of Malware Data Dependency Graph Features}, 
  year={2024},
  volume={},
  number={},
  pages={206-213},
  keywords={Training;Measurement;Accuracy;Semantics;Aerospace electronics;Feature extraction;Malware;machine learning;feature extraction;malware analysis},
  doi={10.1109/NAECON61878.2024.10670673}}

```

# Install
Run:
```
$ git clone https://github.com/musgravejw/ddg-tool
$ cd ./ddg-tool
$ pip install -r ./requirements.txt
$ sudo make install
```

# Usage
- Install
- Run `ddg [source_file]`

## Parameters

### source
This is a path to the binary to be analyzed.

### dest (optional)
This is a destination path for the output file.  It defaults to the current directory.  The output file is a `csv` file containing a list of hashes.  Each hash represents the isomorphic uniqueness of the data dependency graph for each program segment.

# Documentation
Please see `/docs/README`.
  
# License
This project uses the GNU Public License Version 3.  Please see the [LICENSE](https://github.com/musgravejw/ddg-tool/blob/HEAD/LICENSE) for more information.
```
 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
```

# Author
John Musgrave <@musgravejw>, 2019-2022.
