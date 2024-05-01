#include <stdio.h>
#include <unistd.h>

// #includes not shown
int main() {
  fprintf(stdout, "%s", "AAA");
  write(1, "BBB", 3);
  fprintf(stderr, "%s", "CCC");
  return 0;
}