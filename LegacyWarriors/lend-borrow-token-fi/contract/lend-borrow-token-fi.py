import smartpy as sp

# A SmartPy module
@sp.module
def main():
    # A class of contracts
    class Lottery(sp.Contract):
        def __init__(self):
            self.data = sp.record(
                person = {},
                max_lend_amount = sp.tez(10),
                max_amount = sp.tez(200),
            )
            
        @sp.entrypoint
        def lend_tez(self):
            assert self.data.max_amount > sp.tez(0), "NO_AMOUNT_AVAILABLE_LEND"
            assert self.data.max_lend_amount < self.data.max_amount,"INVALID_LEND_AMOUNT"
            self.data.person[sp.len(self.data.person)] = sp.sender
            self.data.max_amount = self.data.max_amount - self.data.max_lend_amount
    
            # Return extra tez balance to the sender
            extra_balance = sp.amount - self.data.max_lend_amount
            if extra_balance > sp.mutez(0):
                sp.send(sp.sender, extra_balance)

        # @sp.entrypoint
        # def end_game(self):
    
        #     # Sanity checks
        #     assert self.data.tickets_available == 0, "GAME_IS_YET_TO_END"
    
        #     # Pick a winner
        #     winner_id = sp.mod(sp.as_nat(sp.now - sp.timestamp(0)), self.data.max_tickets)
        #     winner_address = self.data.players[winner_id]
    
        #     # Send the reward to the winner
        #     sp.send(winner_address, sp.balance)
    
        #     # Reset the game
        #     self.data.players = {}
        #     self.data.tickets_available = self.data.max_tickets


# Tests
if "templates" not in __name__:
    @sp.add_test(name="Lending")
    def test():
        scenario = sp.test_scenario(main)
        scenario.h1("Lending Contract")
        
        admin = sp.test_account("admin")
        alice = sp.test_account("alice")
        bob = sp.test_account("bob")
        mike = sp.test_account("mike")
        charles = sp.test_account("charles")
        john = sp.test_account("john")
    
        scenario.h1("Accounts")
        scenario.show([admin, alice, bob, mike, charles, john])
        lottery = main.Lottery()
        scenario += lottery
        
        # buy_ticket
        scenario.h2("lend_tez (valid test)")
        lottery.lend_tez().run(amount = sp.tez(200), sender = alice)
        lottery.lend_tez().run(amount = sp.tez(200), sender = bob)
        lottery.lend_tez().run(amount = sp.tez(200), sender = john)
        lottery.lend_tez().run(amount = sp.tez(200), sender = charles)
        lottery.lend_tez().run(amount = sp.tez(200), sender = mike)
    
        # scenario.h2("lend_tez (failure test)")
        # lottery.lend_tez().run(amount = sp.tez(1), sender = alice, valid = False)
    
        # end_game
        # scenario.h2("end_game (valid test)")
        # lottery.end_game().run(sender = admin, now = sp.timestamp(20))
