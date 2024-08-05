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
            self._mean = mean
            self._stddev = stddev
            self._usl = usl
            self._lsl = lsl
        else:
            raise TypeError("All arguments must be of type integer or float")

        self._process_capability = (self._usl - self._lsl) / (6 * self._stddev)
        self._process_capability_upper = (self._usl - self._mean) / (3 * self._stddev)
        self._process_capability_lower = (self._mean - self._lsl) / (3 * self._stddev)
        self._process_capability_index = min(
            self._process_capability_upper, self._process_capability_lower
        )
        self._process_accuracy = (self._mean - (self._usl + self._lsl) / 2) / (
            self._usl - self._lsl
        )
        self._process_capability_index_rating = self._calculate_cpk_rating()
        self._process_accuracy_rating = self._calculate_cpa_rating()

        self._metrics = {
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

    # All metrics items calculated above are updated to read-only properties from attributes with the following 8 decorators
    @property
    def metrics(self):
        return self._metrics

    @property
    def process_capability(self):
        return self._process_capability

    @property
    def process_capability_upper(self):
        return self._process_capability_upper

    @property
    def process_capability_lower(self):
        return self._process_capability_lower

    @property
    def process_capability_index(self):
        return self._process_capability_index

    @property
    def process_accuracy(self):
        return self._process_accuracy

    @property
    def process_capability_index_rating(self):
        return self._process_capability_index_rating

    @property
    def process_accuracy_rating(self):
        return self._process_accuracy_rating

    def _calculate_cpk_rating(self) -> str:
        """
        Calculate the rating for the Cpk value.

        Returns:
        - str: The rating of the Cpk value.
        """
        Cpk = self.process_capability_index
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

    def _calculate_cpa_rating(self) -> str:
        """
        Calculate the rating for the Cpa value.

        Returns:
        - str: The rating of the Cpa value.
        """
        Cpa = self.process_accuracy
        if Cpa < 0:
            return "Level A"
        elif Cpa < 0.125:
            return "Level B"
        elif Cpa < 0.25:
            return "Level C"
        else:
            return "Level D"
