import random
import copy
import matplotlib.pyplot as plt

def main():
    # parameter
    EPOCH_NUM = 100
    MANGNIFICATION = 2 # ゲームの倍率

    # const
    INITIAL_BET_ARRAY = [1, 2, 3]

    # balance
    BALANCE = 0

    # result
    gameNum = 0
    maxBet = 0
    minBalance = 0
    balanceRecordArray = []

    for game in range(EPOCH_NUM):
        print("● " + str(game + 1) + "エポック目 スタート")
        betArray = copy.copy(INITIAL_BET_ARRAY)
        while True:
            gameNum += 1
            bet = betArray[0] + betArray[-1]
            if bet > maxBet:
                maxBet = bet
            BALANCE -= bet

            # 勝負開始
            gameResult = random.randrange(MANGNIFICATION)

            if gameResult == 0:
                BALANCE += bet * MANGNIFICATION
                betArray = betArray[1:-1]
                print("  ◯ 勝ち +" + str(bet * MANGNIFICATION) + " | 収支: " + str(BALANCE))

            else:
                if BALANCE < minBalance:
                    minBalance = BALANCE
                betArray.append(bet)
                print("  x 負け -" + str(bet) + " | 収支: " + str(BALANCE))

            # 記録
            balanceRecordArray.append(BALANCE)

            # エポック終了判定
            if not betArray:
                print("----- エポック終了 -----")
                break

    print("*************************************")
    print("- エポック数: " + str(EPOCH_NUM))
    print("- 合計ゲーム数: " + str(gameNum))
    print("- 最終収支: " + "{:,}".format(BALANCE))
    print("- 最低収支: " + "{:,}".format(minBalance))
    print("- 最大ベット: " + "{:,}".format(maxBet))
    print("*************************************")

    plt.plot(range(len(balanceRecordArray)), balanceRecordArray, label="balance")
    plt.grid()
    plt.xlabel("game")
    plt.ylabel("chips")
    plt.legend()
    plt.savefig("result.png")

if __name__ == '__main__':
    main()
