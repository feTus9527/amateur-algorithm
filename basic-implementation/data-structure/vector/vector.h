#ifndef VECTOR_H
#define VECTOR_H

typedef struct vector {
  int size, count;
  int *data;
} vector;

vector *construct_vector(int n);

void destruct_vector(vector *p);

int insert_to_vector(vector *p, int pos, int n);

int remove_from_vector(vector *p, int pos);

int expand_vector(vector *p);
#endif
