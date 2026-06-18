# LeetCode (Python)

My LeetCode solutions, one file per problem.

Files are named `<number>. <Title>.py`. Each one follows the same layout:

- a `# <number>. <Title>` header line
- one block per approach: its name, time/space complexity, and a short
  note on the idea
- assert-based tests at the bottom that run every solution in the file

Most problems keep more than one approach side by side (`Solution`,
`Solution2`, ...), so you can compare the brute-force and the optimized
versions in the same place.

## Running

Run any file directly to check it:

```
python3 "1. Two Sum.py"
```

No output and a zero exit code means the tests passed. A few files use
`sortedcontainers`; install it with `pip install sortedcontainers` if you
hit an import error.
