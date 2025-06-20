from models.functions.function import Function, FunctionParameters, FunctionType
import numpy as np

class AsymmetricLorentzian(Function):
     height: float = 1
     mean: float = 0
     variance_1: float = 1
     variance_2:float = 1 
     
     def __init__(self, function_parameters: FunctionParameters):
        super().__init__(func_type=FunctionType.AsymmetricLorentzian, parameters_num = 4)  # Call base class constructor
        self.height = function_parameters.peaks_height  # Initialize attribute specific to the subclass
        self.mean = function_parameters.tau_guess
        self.variance_1 = function_parameters.peaks_width
        self.variance_2 = function_parameters.peaks_width

     def get_value(self,x):
        return self.height * 1 / (1 + ((x - self.mean) / np.where(x < self.mean, self.variance_1, self.variance_2)) ** 2)
      
     def get_peak(self):
       return self.height
     
     def set_parameters(self,parameters,index):
        if(index < len(parameters)):
          self.height = parameters[index]
          index = index + 1
        if(index < len(parameters)):
          self.mean = parameters[index]
          index = index + 1
        if(index < len(parameters)):
          self.variance_1 = parameters[index]
          index = index + 1
        if(index < len(parameters)):
          self.variance_2 = parameters[index]
          index = index + 1
        return index
     
     def _subclass_dict(self):
        return {"height": self.height, "mean": self.mean, "variance_1": self.variance_1,"variance_2":self.variance_2}
     
     def to_string(self):
        # if self.mean > 0:
        #    return f"\\frac{{{round(self.height, 5)}}}{{cosh(\\frac{{t-{round(self.mean, 5)}}}{{{abs(round(self.alpha, 5))}}})^2}}"
        # if self.mean < 0:
        #     return f"\\frac{{{round(self.height, 5)}}}{{cosh(\\frac{{t+{-round(self.mean, 5)}}}{{{abs(round(self.alpha, 5))}}})^2}}"   
        # return f"\\frac{{{round(self.height, 5)}}}{{cosh(\\frac{{t}}{{{abs(round(self.alpha, 5))}}})^2}}" 
        return ""
     @classmethod
     def from_dict(cls, data):
        # Convert the dictionary back to the PseudoDelta object
        function_parameters = FunctionParameters(
            peaks_height=data["height"],
            tau_guess=data["mean"],
            peaks_width=data["variance"]  # Assuming "variance" is equivalent to "peaks_width"
        )
        return cls(function_parameters=function_parameters)