from pyteal import *
from pyteal_helpers import program

def approval():
    global_owner = Bytes("owner")
    global_first = Bytes("first")
    global_second = Bytes("second")
    global_third = Bytes("third")

    op_result = Bytes("result")

    result1 = Seq(
        App.globalPut(global_first,App.globalGet(global_first) + App.globalGet(global_second)),
        Approve()
    )

    return program.event(
        init=Seq(
            App.globalPut(global_first, Int(10)),
            App.globalPut(global_second, Int(20)),
            App.globalPut(global_third, Int(0)),
            App.globalPut(global_owner, Txn.sender()),
            Approve()
        ),
        no_op=Cond(
            [Txn.application_args[0]==op_result, result1],
        ),
    )

def clear():
    return Approve()