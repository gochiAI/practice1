filename = "/workspace/practice1/out/i.txt"
baseEndpoint = (
  "https://gitlab.com/gochiusa"
  "/DB/Official/Books/main-story/volume1/-/raw/main/Story"
)

with open(filename, 'a') as file:
    for i in range(1, 52):
        file.write(
            f'![]({baseEndpoint}/{str(i).zfill(2)}.png)\r\n'
        )
