import numpy

class Network(object):
    def __init__(self, layers):
        self.layers = layers
        # self.weights = weights
        # self.bias = bias

        self.in_layer = layers[0]
    
    def test_rand(self):
        
        for i in range(10):
            random.seed(5)
            random.randint(0,10)
        
    
    def create_network_randomly(self):
        for i in range(len(self.layers)-1):
            #weight_matrix = np.mat(1 0 0; )
            weigth_string = ""
            for node in self.layers[i+1]:
                for pre_node in self.layers[i]:
                    node.add_weight(w)
                    weigth_string += w + "; "
                    print(w)

            print(weigth_string[:-2])
            weigth_matrice = np.mat(weigth_string[:-2])
            print(weigth_matrice)
    
    def create_network(self):
        for i in range(len(self.layers)-1):
            #weight_matrix = np.mat(1 0 0; )
            weigth_string = ""
            for node in self.layers[i+1]:
                for pre_node in self.layers[i]:
                    w = input("Whats the nodes weight from " + str(pre_node.name) + " to " + str(node.name) + "?")
                    node.add_weight(w)
                    weigth_string += w + "; "
                    print(w)

            print(weigth_string[:-2])
            weigth_matrice = np.mat(weigth_string[:-2])
            print(weigth_matrice)
