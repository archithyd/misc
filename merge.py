#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode :
    def __init__(self, node_data) :
        self.data = node_data
        self.next = None


class SinglyLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def insert_node(self, node_data) :
        node = SinglyLinkedListNode (node_data)

        if not self.head :
            self.head = node
        else :
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data())

        node = node.next



def mergeLists(head1, head2) :
    llist=[]
    temp=head1
    while temp:
        llist.append(temp.data)
        temp=temp.next
    temp=head2
    while temp:
        llist.append(temp.data)
        temp=temp.next
    llist.sort()
    print(llist)
    answer=SinglyLinkedList()
    for i in llist:
        print(i)
        answer.insert_node(i)
    print_singly_linked_list(answer)


if __name__ == '__main__' :


    tests = int (input ( ))

    for tests_itr in range (tests) :
        llist1_count = int (input ( ))

        llist1 = SinglyLinkedList ( )

        for _ in range (llist1_count) :
            llist1_item = int (input ( ))
            llist1.insert_node (llist1_item)

        llist2_count = int (input ( ))

        llist2 = SinglyLinkedList ( )

        for _ in range (llist2_count) :
            llist2_item = int (input ( ))
            llist2.insert_node (llist2_item)

        llist3 = mergeLists (llist1.head, llist2.head)

    print(llist3)