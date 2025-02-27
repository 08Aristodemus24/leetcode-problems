#include <iostream>
#include <cstddef>

// class Node:
//     def __init__(self, data):
//         self.data = data
//         self.next = None

// class LinkedList:
//     def __init__(self):
//         self.head = None

// equivalent to this class implementation of the node and a linked list is the following
struct Node{
    int data;
    Node* next;
};

class LinkedList{
    private:
        // in c++ attributes are declared separately and 
        // assigned a value separately
        // unlike in python, or javascript
        Node* head;

        void _reverse(){

        }

    public:
        LinkedList(){
            head = NULL;
        }

        void insertAtBeginning(int value) {
            // Function to Insert a new node at the beginning of the list
            // time complexity is O(1)

            // a thing to note about using structs as classes is that in C++
            // instead of allocating memory for a node using malloc or calloc
            // using instantiation abstracts this process so that developer won't
            // need to understand in depth the intricacies of memory allocation
            Node* newNode = new Node(); 
            newNode->data = value;      
            newNode->next = head;      
            head = newNode;          
        }

        
        void insertAtEnd(int value) {
            // Function Insert a new node at the end of the list
            // time complexity is O(n) worst case and O(1) best case

            // initialize values of new node to be connected to 
            // end of linked list or if one hasn't been created yet
            // to be the new head
            Node* newNode = new Node(); 
            newNode->data = value;      
            newNode->next = NULL;       

            // If the list is empty, update the head to the new node
            if(!head){
                head = newNode;
                return;
            }

            // Traverse to the last node
            Node* temp = head;
            while(temp->next){
                temp = temp->next;
            }

            // Update the last node's next to the new node
            temp->next = newNode;
        }

        // Function to Insert a new node at a specific position in the list
        void insertAtPosition(int value, int position){
            if(position < 1){
                std::cout << "Position should be >= 1." << std::endl;
                return;
            }

            if(position == 1){
                insertAtBeginning(value);
                return;
            }

            Node* newNode = new Node(); 
            newNode->data = value;     

            // Traverse to the node before the desired position
            Node* temp = head;
            for(int i = 1; i < position - 1 && temp; ++i){
                temp = temp->next;
            }

            // If the position is out of range, print an error message
            if(!temp){
                std::cout << "Position out of range." << std::endl;
                // this deletes the newly allocated node
                delete newNode;
                return;
            }

            // Insert the new node at the desired position
            newNode->next = temp->next;
            temp->next = newNode;
        }

        // Function to Delete the first node of the list
        void deleteFromBeginning(){
            if(!head){
                std::cout << "List is empty." << std::endl;
                return;
            }

            Node* temp = head; 
            head = head->next; 
            delete temp;      
        }

        // Function to Delete the last node of the list
        void deleteFromEnd(){
            if(!head){
                std::cout << "List is empty." << std::endl;
                return;
            }

            if(!head->next){
                delete head;   
                head = NULL;   
                return;
            }

            // Traverse to the second-to-last node
            Node* temp = head;
            while(temp->next->next){
                temp = temp->next;
            }
            
            //  Delete the last node
            delete temp->next; 
            // Set the second-to-last node's next to NULL
            temp->next = NULL; 
        }

        // Function to Delete a node at a specific position in the list
        void deleteFromPosition(int position){
            if(position < 1){
                std::cout << "Position should be >= 1." << std::endl;
                return;
            }

            if(position == 1){
                deleteFromBeginning();
                return;
            }

            Node* temp = head;
            for(int i = 1; i < position - 1 && temp; ++i){
                temp = temp->next;
            }

            if(!temp || !temp->next){
                std::cout << "Position out of range." << std::endl;
                return;
            }

            // Save the node to be deleted
            Node* nodeToDelete = temp->next; 
            // Update the next pointer
            temp->next = temp->next->next;   
            // Delete the node
            delete nodeToDelete;            
        }

        // Function to print the nodes of  the linked list
        void display(){
            if (!head) {
                std::cout << "List is empty." << std::endl;
                return;
            }

            Node* temp = head;
            while(temp){
                std::cout << temp->data << " -> "; 
                temp = temp->next;
            }
            std::cout << "NULL" << std::endl; 
        }

        void reverse(){
            if(!head){
                return;
            }
            // this will be called recursively

            // we will have 3 pointers which will initially
            // be set to null, head, and head->next respectively 
            Node* prev = NULL;
            Node* curr = head;
            Node* next = head->next;

            // we run a while loop 
            while(curr->next != NULL){
                // set the current nodes pointer to
                // point to the previous node
                curr->next = prev;

                // then after setting it we move
                // all three pointers once to the right
                prev = curr;
                curr = next;
                next = next->next;
            }
            // however if curr has already reached the last node we cannot
            // anymore set next to next->next as it will raise an error
            // so we curr's pointer to the previous node to complete the task of 
            // having it be the new head node 
            curr->next = prev;
            
            // finally we set head to the new head which would be the current
            // node having set its pointer to the previous node
            head = curr;
        }
};



int main(int argc, char** argv){
    // this is equivalent to LinkedList ll = new LinkedList();
    LinkedList ll;
    // ll.insertAtEnd(1);
    // ll.insertAtEnd(2);
    // ll.insertAtEnd(3);
    // ll.insertAtEnd(4);
    // ll.insertAtEnd(5);
    ll.display();
    ll.reverse();
    ll.display();

    return 0;
}

