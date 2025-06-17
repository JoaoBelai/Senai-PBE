# classe pai Veiculo que pede capacidade, placa, e custo como atributos obrigatórios
class VeiculoTransporte:
    def __init__(self, capacidade: int, placa: str, custo_km: float):
        self.capacidade = capacidade
        self.placa = placa
        self.custo_km = custo_km

    # método calcular custo que recebe distância e a capacidade atual como parâmetro e retorna o valor da distância pelo custo do km
    def calcular_custo(self, distancia, capacidade_atual):
        total = distancia * self.custo_km
        print(f"\nO valor total da viagem foi: R${total:.2f}")

# subclasse Onibus que herda Veículo
class Onibus(VeiculoTransporte):
    def __init__(self, capacidade, placa, custo_km):
        super().__init__(capacidade, placa, custo_km)
    
    # método calcular custo herdado do pai que retorna o valor da distância pelo custo do km
    # mas caso o veículo esteja com capacidade superior a 80% ele tem um acréscimo de 15% no valor por km
    def calcular_custo(self, distancia, capacidade_atual):
        porcento = (capacidade_atual*100)/self.capacidade
        if porcento > 80:
            self.custo_km = self.custo_km * 1.15
            print("\nDevido a quantidade de pessoas na viagem o custo foi aumentado")
        
        total = distancia * self.custo_km
        print(f"\nO valor total da viagem foi: R${total:.2f}")

# subclasse MicroOnibus que herda Veículo
class MicroOnibus(VeiculoTransporte):
    def __init__(self, capacidade, placa, custo_km):
        super().__init__(capacidade, placa, custo_km)

    # método calcular custo herdado do pai que retorna o valor da distância pelo custo do km
    # mas caso o veículo esteja com capacidade superior a 70% ele tem um acréscimo de 10% no valor por km
    def calcular_custo(self, distancia, capacidade_atual):
        porcento = (capacidade_atual*100)/self.capacidade
        if porcento > 70:
            self.custo_km = self.custo_km * 1.10
            print("\nDevido a quantidade de pessoas na viagem o custo foi aumentado")
        
        total = distancia * self.custo_km
        print(f"\nO valor total da viagem foi: R${total:.2f}")

# subclasse Van que herda Veículo
class Van(VeiculoTransporte):
    def __init__(self, capacidade, placa, custo_km):
        super().__init__(capacidade, placa, custo_km)

    # método calcular custo herdado do pai que retorna o valor da distância pelo custo do km
    # mas caso o veículo esteja com capacidade superior a 60% ele tem um acréscimo de 5% no valor por km
    def calcular_custo(self, distancia, capacidade_atual):
        porcento = (capacidade_atual*100)/self.capacidade
        if porcento > 60:
            self.custo_km = self.custo_km * 1.05
            print("\nDevido a quantidade de pessoas na viagem o custo foi aumentado")
        
        total = distancia * self.custo_km
        print(f"\nO valor total da viagem foi: R${total:.2f}")


#testes
onibus1 = Onibus(20, "ABC-1234", 2.0)
micro_onibus1 = MicroOnibus(15, "ACB-1528", 3.0)
van1 = Van(10, "BAC-3251", 3.5)

onibus1.calcular_custo(100, 10)
onibus1.calcular_custo(100, 19)
micro_onibus1.calcular_custo(100, 7)
micro_onibus1.calcular_custo(100, 15)
van1.calcular_custo(100, 5)
van1.calcular_custo(100, 9)