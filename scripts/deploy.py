from brownie import Swap, Token, config, network, interface
from scripts.help import get_account
from web3 import Web3



KEPT_BALANCE = Web3.toWei(150, "ether")
amounts = Web3.toWei(10, "ether")




def deploy():
	account = get_account()
	# token = Token.deploy({"from": account})
	swap = Swap.deploy(config["networks"][network.show_active()]["weth_token"], config["networks"][network.show_active()]["dao_token"], {"from": account})
	print("DEPLOYED!")


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    print("Approved!")
    return tx


def start_swap():
	account = get_account()
	swap = Swap[-1]
	weth_address = config["networks"][network.show_active()]["weth_token"]
	dao_address = config["networks"][network.show_active()]["dao_token"]
	weth_amount = Web3.toWei(1, "ether")
	dao_amount = Web3.toWei(100, "ether")
	amountToSendWeth = Web3.toWei(0.1, "ether")
	amountToSendDao = Web3.toWei(50, "ether")
	approve_tx_weth = approve_erc20(weth_amount, swap.address, weth_address, account)
	approve_tx_dao = approve_erc20(dao_amount, swap.address, dao_address, account)
	tx = swap.StartSwap(amountToSendWeth, amountToSendDao, {"from": account})
	tx.wait(1)


def setConstant():
	account = get_account()
	swap = Swap[-1]
	tx = swap.setConstant({"from": account})
	tx.wait(1)
	constantNum = swap.constantOfTheSwap({"from": account})
	print("Constant Set!")
	print(f"Constant is {constantNum}")


def swap():
	account = get_account()
	swap = Swap[-1]
	weth_address = config["networks"][network.show_active()]["weth_token"]
	dao_address = config["networks"][network.show_active()]["dao_token"]
	weth_amount = Web3.toWei(1, "ether")
	dao_amount = Web3.toWei(100, "ether")
	amountToSendWeth = Web3.toWei(0.1, "ether")
	amountToSendDao = Web3.toWei(50, "ether")
	approve_tx_weth = approve_erc20(weth_amount, swap.address, weth_address, account)
	approve_tx_dao = approve_erc20(dao_amount, swap.address, dao_address, account)
	tx = swap.swap(weth_address, dao_address, amountToSendWeth, {"from": account})
	tx.wait(1)
	print("SWAP SUCCESFULL!!!")


def showBalance():
	account = get_account()
	swap = Swap[-1]
	tx1, tx2 = swap.showBalance({"from": account})
	print(tx1)
	print(tx2)

def swap2():
	account = get_account()
	swap = Swap[-1]
	token = Token[-1]
	amountsToApprove = Web3.toWei(500, "ether")
	erc20_address = config["networks"][network.show_active()]["weth_token"]
	approve_tx = approve_erc20(amountsToApprove, swap.address, token.address, account)
	amountToSendsss = Web3.toWei(333, "ether")
	tx = swap.swap(token.address, erc20_address, amountToSendsss)
	tx.wait(1)
	print("Swap2 deployed!")



def main():
	deploy()
	start_swap()
	setConstant()
	showBalance()
	swap()
	showBalance()
