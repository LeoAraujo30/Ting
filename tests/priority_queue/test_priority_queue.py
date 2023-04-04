import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 9})
    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 2})
    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 7})
    queue.enqueue({"qtd_linhas": 11})
    queue.enqueue({"qtd_linhas": 3})

    assert queue.high_priority.data + queue.regular_priority.data == [
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 3},
        {"qtd_linhas": 9},
        {"qtd_linhas": 5},
        {"qtd_linhas": 7},
        {"qtd_linhas": 11}
    ]

    queue.dequeue()
    queue.dequeue()

    assert queue.high_priority.data + queue.regular_priority.data == [
        {"qtd_linhas": 3},
        {"qtd_linhas": 9},
        {"qtd_linhas": 5},
        {"qtd_linhas": 7},
        {"qtd_linhas": 11}
    ]

    assert queue.search(3) == {"qtd_linhas": 7}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(10)
