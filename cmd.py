import subprocess # Стандартний інструмент для виклику підпроцессів (наприклад консолі)
model_path = "...\stable-diffusion-v1-5-pruned-emaonly-Q8_0.gguf" # Змінити на адресу власної моделі
# prompt = "beach sea waves palm tree"
prompt = ""
output = "result.png"

# Reading data from file
with open('prompt.txt', 'r') as file:
    prompt = file.read()

print(f"prompt: {prompt}")
cmd = [
    #"python", # Шлях до програми, що маємо запустити sd.exe
    "...\sd.exe",
    "--model", model_path,
    "--prompt", prompt,
    "--output", output,
    "--width", "512",
    "--height", "512",
    "--steps", "30",
    "--seed", "42",
]

subprocess.run(cmd)