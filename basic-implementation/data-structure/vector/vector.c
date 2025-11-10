#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "vector.h"

Vector *construct_vector(int n) {
  Vector *p = (Vector *)malloc(sizeof(Vector));
  p->size = n;
  p->count = 0;
  p->data = (int *)malloc(sizeof(int) * n);
  return p;
}

void destruct_vector(Vector *p) {
  if (p == NULL) {
    return;
  }
  free(p->data);
  free(p);
}

int insert_to_vector(Vector *p, int pos, int n) {
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

int remove_from_vector(Vector *p, int pos) {
  if (pos < 0 || pos >= p->count) {
    return 0;
  }
  for (int i = pos; i <= p->count - 1; i++) {
    p->data[i] = p->data[i + 1];
  }
  p->count -= 1;
  return 1;
}

int expand_vector(Vector *v) {
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

void print_vector(Vector *v) {
  if (v == NULL || v->size == 0) {
    printf("Empty vector\n");
    return;
  }

  int *widths = (int *)malloc(v->size * sizeof(int));
  if (widths == NULL) {
    printf("Memory allocation failed\n");
    return;
  }

  int total_width = 0;
  for (int i = 0; i < v->size; i++) {
    int index_width = snprintf(NULL, 0, "%d", i);
    int data_width = snprintf(NULL, 0, "%d", v->data[i]);
    widths[i] = index_width > data_width ? index_width : data_width;
    total_width += widths[i];
  }

  total_width += (v->size - 1);

  printf("┌─");
  for (int i = 0; i < total_width; i++) {
    printf("─");
  }
  printf("─┐\n");

  printf("│ ");
  for (int i = 0; i < v->size; i++) {
    printf("%*d", widths[i], i);
    if (i < v->size - 1) {
      printf(" ");
    }
  }
  printf(" │\n");

  printf("├─");
  for (int i = 0; i < total_width; i++) {
    printf("─");
  }
  printf("─┤\n");

  printf("│ ");
  for (int i = 0; i < v->size; i++) {
    printf("%*d", widths[i], v->data[i]);
    if (i < v->size - 1) {
      printf(" ");
    }
  }
  printf(" │\n");

  printf("└─");
  for (int i = 0; i < total_width; i++) {
    printf("─");
  }
  printf("─┘\n\n");

  free(widths);
}

int main(int argc, char *argv[]) {
  srand(time(0));
#define TOTAL_OPS 20
#define VECTOR_LENGTH 2
#define N_MAX 10000
#define INSERT_RATIO 75
#define POSITION_OVERFLOW 2

  Vector *v = construct_vector(VECTOR_LENGTH);

  for (int i = 0; i < TOTAL_OPS; i++) {
    int op = rand() % 100;
    int pos = rand() % (v->count + POSITION_OVERFLOW);
    if (op < INSERT_RATIO) {
      int val = rand() % N_MAX;
      printf("insert item %d at %d to vector = %d\n", val, pos,
             insert_to_vector(v, pos, val));
    } else {
      printf("delete item at %d from vector = %d\n", pos,
             remove_from_vector(v, pos));
    }
    print_vector(v);
  }
  destruct_vector(v);
}
