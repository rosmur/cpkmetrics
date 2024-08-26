from src.utils.tableprinter import print_table
import math


class ProcessCapability:
    """
    A class to calculate process capability metrics and their ratings.
    """

    def __init__(
        self,
        mean: float | int,
        stddev: float | int,
        usl: float | int | None = None,
        lsl: float | int | None = None,
        print_results=True,
    ):
        """
        Initialize the ProcessCapability class with the necessary parameters.

        Parameters:
        - mean (float | int): The mean of the process.
        - stddev (float | int): The standard deviation of the process.
        - usl (float | int | None): The upper specification limit.
        - lsl (float | int | None): The lower specification limit.

        Raises:
        - TypeError: If any of the arguments are not of type integer or float.
        """

        # Type checking prior to assignment
        if all(
            isinstance(arg, (float, int, type(None)))
            for arg in [mean, stddev, usl, lsl]
        ):
            self._mean = mean
            self._stddev = stddev
            self._usl = usl
            self._lsl = lsl
        else:
            raise TypeError("All arguments must be of type integer or float")

        # Set USL/LSL to None if it is an empty value (NaN). This makes the subsequent cleaner/more readable.
        if math.isnan(self._usl):
            self._usl = None
        if math.isnan(self._lsl):
            self._lsl = None

        # Calculate Cp and Cpa
        if self._usl is not None and self._lsl is not None:
            self._process_capability = (self._usl - self._lsl) / (6 * self._stddev)
            self._process_accuracy = (self._mean - (self._usl + self._lsl) / 2) / (
                self._usl - self._lsl
            )
            self._process_accuracy_rating = self._calculate_cpa_rating()
        else:
            self._process_capability = None
            self._process_accuracy = None
            self._process_accuracy_rating = None

        # Calculate Cpu, Cpl
        self._process_capability_upper = (
            (self._usl - self._mean) / (3 * self._stddev)
            if self._usl is not None
            else None
        )
        self._process_capability_lower = (
            (self._mean - self._lsl) / (3 * self._stddev)
            if self._lsl is not None
            else None
        )

        # Calculate Cpk
        if (
            self._process_capability_upper is not None
            and self._process_capability_lower is not None
        ):
            self._process_capability_index = min(
                self._process_capability_upper, self._process_capability_lower
            )
        elif self._process_capability_upper is not None:
            self._process_capability_index = self._process_capability_upper
        elif self._process_capability_lower is not None:
            self._process_capability_index = self._process_capability_lower
        else:  # Case when both USL and LSL are None
            self._process_capability_index = None

        # Calculate Sigma Level and Cpk Rating
        if self.process_capability_index is not None:
            self._sigma_level = int(
                (self.process_capability_index * 3) // 1
            )  # Extracting quotient and then making an integer
            self._process_capability_index_rating = self._calculate_cpk_rating()
        else:
            self._sigma_level = None
            self._process_capability_index_rating = None

        self._metrics = {
            "Process Capability": self.process_capability,
            "Process Capability Index": self.process_capability_index,
            "Process Capability Upper": self.process_capability_upper,
            "Process Capability Lower": self.process_capability_lower,
            "Process Accuracy": self.process_accuracy,
            "Process Sigma Level": self.sigma_level,
            "Process Capability Index Rating": self.process_capability_index_rating,
            "Process Accuracy Rating": self.process_accuracy_rating,
        }

        if print_results and self._usl is None and self._lsl is None:
            print(
                "Both USL and LSL have not been provided. Process capability metrics cannot be computed"
            )
        elif print_results:
            print_table(self.metrics)

    # All metrics items calculated above are made available as read-only properties from attributes with the following 8 decorators
    @property
    def metrics(self) -> dict:
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

    @property
    def sigma_level(self):
        """
        The sigma level that the process is operating at: it is 3 Sigma level if it is 1-1.33, 4 Sigma between 1.33-1.67, 5 Sigma between 1.67-2 and so forth.
        It is numerically effectively the value of Cpk if there was no division by 3, i.e. it is equal to Cpk multiplied by 3 and rounded down to the nearest integer.
        """
        if self._sigma_level is None:
            return None
        elif self._sigma_level <= 0:
            return "Completely out of specification"
        elif 0 < self._sigma_level <= 9:
            return f"{self._sigma_level}\u03c3"
        elif self._sigma_level > 3:
            return "Abnormally High"
        else:
            raise ValueError

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
        cpa = abs(self.process_accuracy)
        if cpa < 0.125:
            return "Level A"
        elif cpa < 0.25:
            return "Level B"
        elif cpa < 0.5:
            return "Level C"
        else:
            return "Level D"
