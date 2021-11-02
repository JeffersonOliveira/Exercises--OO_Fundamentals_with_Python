from conta import Conta


conta1 = Conta(1,'Jefferson',2500.0)
conta1.__dict__
conta1.deposita(300.0)
conta1.extrato()
conta1.saca(100.0)
conta1.extrato()