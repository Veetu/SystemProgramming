def main():
    numN = int(input("Give value of n: "))
    numK = int(input("Give value of k: "))
    binomi = Binomi(numN, numK)
    binomi.calculate_binomi()
class Binomi():



    def __init__(self, numN, numK):
        self.numN = numN
        self.numK = numK


    def calculate_binomi(self):

        saveN = 1.0
        saveK = 1.0
        saveNK = 1.0

        if self.numK > self.numN or self.numN <= 0:
            values = False

        else:
            for x in range(self.numN):
                saveN = saveN * (x +1)
            for x in range(self.numK):
                saveK = saveK * (x +1)
            for x in range(self.numN - self.numK):
                saveNK = saveNK * (x +1)




        values = saveN / (saveK * (saveNK))


        print("Value of n choose k = " , values)
        return values

if __name__ == "__main__":
    main()