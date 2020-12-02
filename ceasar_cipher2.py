from art import caesar_cipher_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def init():
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25 or shift < -25:
    shift = shift % 26
  caesar_cipher(word = text, s= shift, task =direction)
  r = input("Do you want to repeat? Y for yes").lower()
  if r == 'y':
    init()
    r = 'n'
  else:
    print("Goodbye!")

def caesar_cipher(word, s, task):
  if task == 'encode' or task == 'decode':
    st = ""
    for i in word:
      if i in alphabet:
        index = alphabet.index(i)
        if task == 'encode':
          if s >= 0:
            index += s
          if s < 0:
            index -= s
          if index > 25:
            index = index - 26

        elif task == 'decode':
          if s >= 0:
            index -= s
          if s < 0:
            index += s    
        st = st + alphabet[index]
      else:
        st = st + i
    print("The "+task+"d message is: "+st)
  else:
    print("Wrong input!")
    exit()

init()
