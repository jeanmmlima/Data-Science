#jogando dado 6 vezes, quala media
#jogando dado 100000 vezes, media aproximada = 3,5
x = 0
for (i in 1:100000)
  (
    x = x + sample(1:6,1)
  )

x = x / 100000
x

####################
####################



