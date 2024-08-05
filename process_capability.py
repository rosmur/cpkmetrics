from utils.tableprinter import print_table


class ProcessCapability:
    """
    A class to calculate process capability metrics and their ratings.
    """

    def __init__(
        self,
        mean: float | int,
        stddev: float | int,
        usl: float | int,
        lsl: float | int,
        print_results=True,
    ):
        """
        Initialize the ProcessCapability class with the necessary parameters.

        Parameters:
        - mean (float): The mean of the process.
        - stddev (float): The standard deviation of the process.
        - usl (float): The upper specification limit.
        - lsl (float): The lower specification limit.
        """
        if all(isinstance(arg, (float, int)) for arg in [mean, stddev, usl, lsl]):
            self.mean = mean
            self.stddev = stddev
            self.usl = usl
            self.lsl = lsl
        else:
            raise TypeError("All arguments must be of type integer or float")

        self.process_capability = self.Cp()
        self.process_capability_index = self.Cpk()
        self.process_capability_upper = self.Cpu()
        self.process_capability_lower = self.Cpl()
        self.process_accuracy = self.Cpa()
        self.process_capability_index_rating = self.Cpk_rating()
        self.process_accuracy_rating = self.Cpa_rating()

        self.metrics = {
            "Process Capability": self.process_capability,
            "Process Capability Index": self.process_capability_index,
            "Process Capability Upper": self.process_capability_upper,
            "Process Capability Lower": self.process_capability_lower,
            "Process Accuracy": self.process_accuracy,
            "Process Capability Index Rating": self.process_capability_index_rating,
            "Process Accuracy Rating": self.process_accuracy_rating,
        }

        if print_results:
            print_table(self.metrics)

    #     self.metrics()

    # @property
    # def metrics(self):
    #     return self._metrics

    def Cp(self):
        """
        Calculate Cp (Process Capability).

        Returns:
        - float: The process capability value.
        """
        return (self.usl - self.lsl) / (6 * self.stddev)

    def Cpu(self):
        """
        Calculate Cpu (Process Capability Upper).

        Returns:
        - float: The process capability upper value.
        """
        return (self.usl - self.mean) / (3 * self.stddev)

    def Cpl(self):
        """
        Calculate Cpl (Process Capability Lower).

        Returns:
        - float: The process capability lower value.
        """
        return (self.mean - self.lsl) / (3 * self.stddev)

    def Cpk(self):
        """
        Calculate Cpk (Process Capability Index).

        Returns:
        - float: The process capability index value.
        """
        return min(
            (self.usl - self.mean) / (3 * self.stddev),
            (self.mean - self.lsl) / (3 * self.stddev),
        )

    def Cpa(self):
        """
        Calculate Cpa (Process Capability Accuracy).

        Returns:
        - float: The process capability accuracy value.
        """
        return (self.mean - (self.usl + self.lsl) / 2) / (self.usl - self.lsl)

    def Cpk_rating(self):
        """
        Rate the Cpk value.

        Returns:
        - str: The rating of the Cpk value.
        """
        Cpk = self.Cpk()
        if Cpk <= 0:
            return "Abnormally Poor"
        elif 0 < Cpk <= 0.5:
            return "Poor"
        elif 0.5 < Cpk <= 1:
            return "Low"
        elif 1 < Cpk <= 1.33:
            return "Good"
        elif 1.33 < Cpk <= 1.67:
            return "Great"
        elif 1.67 < Cpk <= 2:
            return "Excellent"
        elif Cpk > 2:
            return "Abnormally High"
        else:
            raise ValueError

    def Cpa_rating(self):
        """
        Rate the Cpa value.

        Returns:
        - str: The rating of the Cpa value.
        """
        Cpa = self.Cpa()
        if Cpa < 0:
            return "Level A"
        elif Cpa < 0.125:
            return "Level B"
        elif Cpa < 0.25:
            return "Level C"
        else:
            return "Level D"
