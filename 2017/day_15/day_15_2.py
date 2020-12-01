# --- Day 15: Dueling Generators ---
# Part 2 - OK

class Gen:

    def __init__(self, seed, factor, criteria):
        self.current = seed
        self.factor = factor
        self.criteria = criteria

    def __iter__(self):
        return self

    def __next__(self):
        """
        Calculate next
        To create its next value, a generator will take the previous value
        it produced, multiply it by a factor (generator A uses 16807;
        generator B uses 48271), and then keep the remainder of dividing
        that resulting product by 2147483647.
        :return:
        """

        # calc new value and save it as prev.

        while True:
            value = self.current * self.factor
            self.current = value % 2147483647

            if (self.current % self.criteria) == 0:
                return self.current

    def __eq__(self, other):
        """
        Test if the 16 last bits in the current number equals the other
        generator.
        :param other:
        :return:
        """
        return self.get_16_bits() == other.get_16_bits()

    def get_16_bits(self):
        return 65535 & self.current

    def __str__(self):
        return str(self.current)

    def __format__(self, format_spec):
        return self.__str__()


if __name__ == '__main__':

    gen_a = Gen(seed=783, factor=16807, criteria=4)
    gen_b = Gen(seed=325, factor=48271, criteria=8)
    #gen_a = Gen(seed=65, factor=16807, criteria=4)
    #gen_b = Gen(seed=8921, factor=48271, criteria=8)

    matches = 0
    for i in range(5000000):
        # Get the new values
        next(gen_a)
        next(gen_b)

        if i % 1000000 == 0:
            print(i)

        if gen_a == gen_b:
            matches = matches + 1


    print("Found {} matches!".format(matches))
