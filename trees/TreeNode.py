from problog.program import SimpleProgram
from problog.logic import *

class FOLDecisitionTree:
    """A First-Order Logical Decision Tree"""
    root_node = None

    def __init__(self, example_list):
        root_node = TreeNode()
        query = True
        root_node.build_tree(example_list, query)


class TreeNode:
    """A node in a First-Order Logical Decision Tree.

    There are two kinds of nodes: decision nodes and leaf nodes"""
    left_subtree = None
    right_subtree = None

    conj = True
    query = True
    classification = None

    # def build_tree(self, example_list):
    #     # check if the tree is homogeneous
    #     homogeneous_check =\
    #         is_current_example_set_sufficiently_homogenous(example_list)
    #     if homogeneous_check:
    #         return
    #     else:
    #         refined_query = get_best_refined_query(self.query, example_list)


def decision_tree_to_simple_program(node, simple_program, previous_conjunction = Term('true')):
    # if the current node is a leaf
    if node.left_subtree is None and node.right_subtree is None:
        if node.classification is not None:
            clause = (node.classification << previous_conjunction)
            simple_program += clause
            return [node.classification]
        else:
            raise InvalidTreeNodeError()
    else:
        # for the left subnode
        total_conj_left_node = And(previous_conjunction, node.conj)
        left_class_labels = decision_tree_to_simple_program(node.left_subtree, simple_program, total_conj_left_node)

        # for the right subnode
        negated_left_class_labels = [~label for label in left_class_labels]
        conj_of_neg_left_class_ables = And.from_list(negated_left_class_labels)
        total_conj_right_node = And(conj_of_neg_left_class_ables, previous_conjunction)
        right_class_labels = decision_tree_to_simple_program(node.right_subtree, simple_program, total_conj_right_node)
        return left_class_labels + right_class_labels


def decision_tree_to_simple_program2(node, simple_program, previous_conjunction=Term('true')):

    if node.left_subtree is not None and node.left_subtree is not None:
        # assign a new predicate to this node
        p = generate_new_predicate()
        conj_left = And(previous_conjunction, node.conj)
        conj_right = And(previous_conjunction, ~p)
        clause = (p << conj_left)
        simple_program += clause

        # recurse on left subtree
        decision_tree_to_simple_program2(node.left_subtree,simple_program, conj_left)
        # recurse on right subtree
        decision_tree_to_simple_program2(node.left_subtree, simple_program, conj_right)
    else:
        if node.classification is not None:
            clause = (node.classification << previous_conjunction)
            simple_program += clause
        else:
            raise InvalidTreeNodeError()


class InvalidTreeNodeError(Exception):
    pass
