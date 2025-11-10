#ifndef VECTOR_H
#define VECTOR_H

typedef struct Vector {
  int size, count;
  int *data;
} Vector;

Vector *construct_vector(int n);

void destruct_vector(Vector *p);

int insert_to_vector(Vector *p, int pos, int n);

int remove_from_vector(Vector *p, int pos);

int expand_vector(Vector *p);
#endif
