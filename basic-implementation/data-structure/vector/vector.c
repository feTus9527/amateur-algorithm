#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "vector.h"

vector *construct_vector(int n) {
  vector *p = (vector *)malloc(sizeof(vector));
  p->size = n;
  p->count = 0;
  p->data = (int *)malloc(sizeof(int) * n);
  return p;
}

void destruct_vector(vector *p) {
  if (p == NULL) {
    return;
  }
  free(p->data);
  free(p);
}

int insert_to_vector(vector *p, int pos, int n) {
  if (pos < 0 || pos > p->count) {
    return 0;
  }
  if (p->size == p->count && !expand_vector(p)) {
    return 0;
  }
  for (int i = p->count; i >= pos; i--) {
    p->data[i] = p->data[i - 1];
  }
  p->data[pos] = n;
  p->count += 1;
  return 1;
}

int remove_from_vector(vector *p, int pos) {
  if (pos < 0 || pos >= p->count) {
    return 0;
  }
  for (int i = pos; i <= p->count - 1; i++) {
    p->data[i] = p->data[i + 1];
  }
  p->count -= 1;
  return 1;
}

int expand_vector(vector *v) {
  if (v == NULL) {
    return 0;
  }
  int *newData = (int *)realloc(v->data, sizeof(int) * 2 * v->size);
  if (newData == NULL) {
    return 0;
  }
  v->data = newData;
  v->size *= 2;
  return 1;
}

void print_vector(vector *v) {
  int len = 0;
  for (int i = 0; i < v->size; i++) {
    len += printf("%3d", i);
  }
  printf("\n");
  for (int i = 0; i < len; i++)
    printf("-");
  printf("\n");
  for (int i = 0; i < v->size; i++) {
    printf("%3d", v->data[i]);
  }
  printf("\n\n");
}

int main(int argc, char *argv[]) {
  srand(time(0));
#define MAX_OP 20
#define VECTOR_LENGTH 2
  vector *v = construct_vector(VECTOR_LENGTH);
  for (int i = 0; i < MAX_OP; i++) {
    int op = rand() % 4, pos, val;
    switch (op) {
    case 0:
    case 1:
    case 2:
      pos = rand() % (v->count + 2);
      val = rand() % 100;
      printf("insert item %d at %d to vector = %d\n", val, pos,
             insert_to_vector(v, pos, val));
      break;
    case 3:
      pos = rand() % (v->count + 2);
      printf("delete item at %d from vector = %d\n", pos,
             remove_from_vector(v, pos));
      break;
    }
    print_vector(v);
  }
  destruct_vector(v);
}
