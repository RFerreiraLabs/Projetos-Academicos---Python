metro = float(input('Digite a metragem desejada: '))
cent = metro * 100
milim = metro * 1000
km = metro / 100

input('A conversão de {}m em centimetros é {:.0f}cm e em milimetros é {:.0f}mm'.format(metro, cent, milim))
