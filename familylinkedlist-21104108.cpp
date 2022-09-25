#include <iostream>
using namespace std;

class node
{

public:
    string name;
    int data;

    node *next;
    node *prev;

    node(string d, int age)
    {
        name = d;
        data = age;
        next = NULL;
        prev = NULL;
    }
};

void insertAtFirst(node *&head, string d, int age)
{

    node *n = new node(d, age);
    n->next = head;
    if (head != NULL)
    {
        head->prev = n;
    }

    head = n;
}

void insertAtTail(node *&head, string d, int age)
{
    if (head == NULL)
    {
        insertAtFirst(head, d, age);
        return;
    }

    node *n = new node(d, age);
    node *temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = n;
    n->prev = temp;
}
void display(node *head)
{
    node *temp = head;
    while (temp != NULL)
    {

        cout << temp->name << " " << temp->data << endl;
        temp = temp->next;
    }
}
int main()
{
    node *head = NULL;
    cout << "Displaying the family members with their ages" << endl;
    insertAtTail(head, "Father", 40);
    insertAtTail(head, "Mother", 38);
    insertAtTail(head, "Brother", 18);
    insertAtTail(head, "Sister", 16);
    display(head);
    cout << endl;

    cout << "After inserting the family member " << endl;
    insertAtTail(head, "Grandmother", 60);
    display(head);
}