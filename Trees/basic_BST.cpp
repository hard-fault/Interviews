#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

struct node{
    int data;
    struct node *left, *right;
};

struct node *newnode=NULL;

struct node* insert(struct node **root, int data) 
{
    if(*root == NULL)
    {
        newnode = (struct node*) malloc (sizeof(struct node));
        newnode->data = data;
        newnode->left = NULL;
        newnode->right = NULL;
        *root=newnode; 
    }

    if(data > (*root)->data )
        (*root)->right = insert(&((*root)->right),data);
    else if(data < (*root)->data)
        (*root)->left = insert(&((*root)->left),data);
    
    return *root;
}

void inorder(struct node* root)
{
    if(root!=NULL)
    {
        inorder(root->left);
        cout<<root->data<<",";
        inorder(root->right);
    }
}

void mirror(struct node* root1, struct node* root2)
{

}

int main()
{
    //int a[]={16,12,23,5,14,19,25};
    int a[]={16,12,5,14,23,19,25};
    int n=sizeof(a)/sizeof(a[0]);
    struct node *root=NULL;
    
    for(int i=0;i<n;i++)
        insert(&root,a[i]);
    
    cout<<"\nInorder traversal\n";
    inorder(root);
    cout<<endl;
    
    return 0;
}
