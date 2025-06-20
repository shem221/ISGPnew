from models.functions.function import Function, FunctionParameters, FunctionType
import numpy as np

class Losev(Function):
     height: float = 1
     mean: float = 0
     variance_1: float = 1
     variance_2:float = 1 
     
     def __init__(self, function_parameters: FunctionParameters):
        super().__init__(func_type=FunctionType.Losev, parameters_num = 4)  # Call base class constructor
        self.height = function_parameters.peaks_height  # Initialize attribute specific to the subclass
        self.mean = function_parameters.tau_guess
        self.variance_1 = function_parameters.peaks_width
        self.variance_2 = function_parameters.peaks_width

     def get_value(self,x):
        return  self.height / (np.exp(-x /self.variance_1) + np.exp(x / self.variance_2))
      
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

        return ""
     
     @classmethod
     def from_dict(cls, data):
        # Convert the dictionary back to the ColeCole object
        function_parameters = FunctionParameters(
            peaks_height=data["height"],
            tau_guess=data["mean"],
            peaks_width=data["variance"]
        )
        return cls(function_parameters=function_parameters)  # Pass alpha as an argument