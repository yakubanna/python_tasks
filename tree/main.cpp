#include <iostream>
#include <algorithm>
#include <utility>
#include <stack>
#include <string>

const int MOD = 1E9 + 7;

struct node {
    char key;
    int priority;
    int cnt;
    bool rvs;
    node *left, *right;
    explicit node(char key) : key(key), priority(rand()% MOD),
                    cnt(1), rvs(false),
                    left(nullptr), right(nullptr) {}
};

int cnt(node* &root) {
    if (!root) {
        return 0;
    }
    return root->cnt;
}

void upd_cnt(node* &root) {
    if (root) {
        root->cnt = 1 + cnt(root->left) + cnt(root->right);
    }
}

void push(node* &root) {
    if (root && root->rvs) {
        root->rvs = false;
        std::swap(root->left, root->right);
    if (root->left != nullptr) {
        root->left->rvs ^= true;
    }
    if (root->right != nullptr) {
        root->right->rvs ^= true;
    }
  }
}

void merge(node* &root, node* T1_, node* T2_) {
    push(T1_);
    push(T2_);
    if (!T1_ || !T2_) {
        root = T1_ ? T1_ : T2_;
        return;
    }
    if (T1_->priority > T2_->priority) {
        merge(T1_->right, T1_->right, T2_);
        root = T1_;
    } else {
        merge(T2_->left, T1_, T2_->left);
        root = T2_;
    }
    upd_cnt(root);
}

void split(node* root, int key, node* &left, node* &right, int add = 0) {
    if (!root) {
        left = right = nullptr;
        return;
    }
    push(root);
    int cur_key = add + cnt(root->left);
    if (cur_key < key) {
        split(root->right, key, root->right, right, add + 1 + cnt(root->left));
        left = root;
    } else {
        split(root->left, key, left, root->left, add);
        right = root;
    }
    upd_cnt(root);
}

void insert(node* &root, int idx, char key) {
    node* new_node = new node(key);
    if (!root) {
        root = new_node;
        return;
    }
    node* left, *right;
    split(root, idx, left, right);
    merge(left, left, new_node);
    merge(root, left, right);
    upd_cnt(root);
}

void inorder(node* root) {
    if (root) {
        push(root);
        inorder(root->left);
        std::cout << root->key;
        inorder(root->right);
    }
}

void reverse_query(node *root, int a_, int b_) {
    node *T1_, *T2_, *T3_;
    split (root, a_, T1_, T2_);
    split (T2_, b_ - a_ + 1, T2_, T3_);
    T2_->rvs = true;
    merge(root, T1_, T2_);
    merge(root, root, T3_);
}

std::stack<std::pair<std::pair<int, int>, int>> arr;

int main() {
    node* root = nullptr;
    int a_, b_, s_, sz = 0, amount;
    std::string str;
    std::cin >> str;
    int size = str.size();
    for (int i = 0; i < size; ++i) {
        insert(root, sz++, str[i]);
    }
    std::cin >> amount;
    while (amount--) {
        std::cin >> a_ >> b_ >> s_;
        arr.push(std::make_pair(std::make_pair(--a_, --b_), s_));
    }
    while (not arr.empty()) {
        a_ = arr.top().first.first;
        b_ = arr.top().first.second;
        s_ = arr.top().second;
        arr.pop();
        s_ = b_ - a_ + 1 - s_;
        reverse_query(root, a_, b_);
        reverse_query(root, a_, a_ + s_ - 1);
        reverse_query(root, a_ + s_, b_);
    }
    inorder(root);
    return 0;
}