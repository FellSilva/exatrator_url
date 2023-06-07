endereco = "rua flores 72, apatamento 1002,laranjeiras, Rio de Janeiro, RJ,23740-120"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
   cep = busca.group()
   print(cep)

