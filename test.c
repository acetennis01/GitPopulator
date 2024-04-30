#include <stdio.h>
#include <unistd.h>

int main() {
  fprintf(stdout, "%s", "AAA");
  write(1, "BBB", 3);
  fprintf(stderr, "%s", "CCC");
  return 0;
}