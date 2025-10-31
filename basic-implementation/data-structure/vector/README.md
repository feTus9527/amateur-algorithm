# Vector

## Attributes

A vector implementation must maintain the following attributes: 

| Name  | Type      | Description                                                  |
| ----- | --------- | ------------------------------------------------------------ |
| count | integer   | The number of elements currently stored in the vector.       |
| size  | integer   | The total capacity of the vector (maximum elements without resizing). |
| data  | integer[] | The underlying array containing all elements, stored contiguously in memory. |

## Operations

1. **Initialization**: Create a new vector with specified capacity.
   - **Input**: Integer `n` representing initial capacity
   - **Output**: A new vector instance with capacity `n`
2. **Insertion Operations**:
   - **Append**: Add an element to the end of the vector.
     - **Input**: Integer  `n`  to be appended.
     - **Effect**: Element is added at position `count`, and `count` is incremented.
   - **Insert at Position**: Insert an element at a specific position within the vector.
     - **Input**: Integer `n` to insert, index `pos` specifying insertion position
     - **Effect**: Element is inserted at position `pos`, shifting subsequent elements
     - **Note**: Requires `0 ≤ pos ≤ count`
3. **Removal**: Remove the element at a specified position.
   - **Input**: Index `pos` of element to remove
   - **Effect**: Element at position `pos` is removed, subsequent elements shifted left
   - **Note**: Requires `0 ≤ pos < count`
4. **Capacity Management**:
   - **Automatic Expansion**: When a vector reaches its capacity, it must be expanded automatically.
     - **Trigger**: Insertion operation when `count` equals `size`
     - **Effect**: Allocates new, larger memory block and transfers existing elements
5. **Access Operations**:
   - **Access All Data**: Retrieve the entire underlying array.
     - **Output**: Reference to the vector's data array
   - **Access Element by Index**: Retrieve the element at a specific position.
     - **Input**: index `pos`
     - **Output**: Element value at position `pos`
     - **Note**: Requires `0 ≤ pos < count`
   - **Get Capacity**: Retrieve the vector's total capacity.
     - **Output**: Integer representing the vector's `size` attribute
   - **Get Element Count**: Retrieve the number of elements in the vector.
     - **Output**: Integer representing the vector's `count` attribute
