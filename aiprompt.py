import tkinter as tk
import threading
from asyncio import threads
import undetected_chromedriver as uc
from pywinauto.handleprops import controlid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import shutil
import pywinauto.application as Application
from PIL import Image, ImageTk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
value1="val"
def val1():
    global value1
    value1="chatgpt"

def sreek1():
    directory_to_search = "C:\\"  # Or specify the absolute path
    gguf_filename = "appicon.jpg"

    found_path1 = find_gguf_file(directory_to_search, gguf_filename)
    return found_path1
def see():
    directory_to_search = "C:\\"  # Or specify the absolute path
    gguf_filename = "koboldcpp.exe"

    found_path2 = find_gguf_file(directory_to_search, gguf_filename)
    return found_path2
def pre():
    directory_to_search = "C:\\"  # Or specify the absolute path
    gguf_filename = "koboldcpp.exe"

    found_path2 = find_gguf_file(directory_to_search, gguf_filename)

    if found_path2:
        return True
    else:
        return False

def find_gguf_file(directory, filename):
    for root, _, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def gguf():
    directory_to_search = "C:\\"  # Or specify the absolute path
    gguf_filename = "Qwen3-Coder-30B-A3B-Instruct-UD-TQ1_0.gguf"

    found_path = find_gguf_file(directory_to_search, gguf_filename)

    if found_path:
        return True
    else:
        return False
def serv():

    if pre() == True:
       pass

    if pre() == False:
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)
        # chromedriver_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        # service = Service(executable_path=chromedriver_path)
        # driver = webdriver.Chrome(service=service)
        driver.get("https://github.com/LostRuins/koboldcpp/releases/tag/v1.97.2")
        download_link = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "koboldcpp.exe"))
        )
        download_link.click()
        time.sleep(300)
        driver.close()
    if gguf() == False:
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)
        driver.get("https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF/blob/main/Qwen3-Coder-30B-A3B-Instruct-UD-TQ1_0.gguf")
        download_link1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "download")))
        download_link1.click()
        time.sleep(1200)
        driver.close()
    else:
        print("gguf")
    app = Application.Application(backend="uia")
    app.start(f'{see()} --skiplauncher --model "C:\\Users\\psybe\\Downloads\\Qwen3-4B-Thinking-2507-UD-Q5_K_XL.gguf"', wait_for_idle = False)
    #main=app.window(title="Select ggml model .bin or .gguf file or .kcpps config")
    #main.child_window(title="File name:",control_type="ComboBox").set_text("Qwen3-4B-Thinking-2507-UD-Q5_K_XL.gguf")
    #main.Filename.set_edit_text("Qwen3-4B-Thinking-2507-UD-Q5_K_XL.gguf")
    #main_window.("C:\\Users\\psybe\\Downloads\\Qwen3-4B-Thinking-2507-UD-Q5_K_XL.gguf")
    time.sleep(20)
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get("http://localhost:5001")
    cancel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='popupfooter']/button[text()='Cancel']"))
    )
    cancel_button.click()
    #cancel_top = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "popupfooter")))
    #cancels=cancel_top.find_element(By.PARTIAL_LINK_TEXT,"Cancel")
    #cancels.click()
    texton = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='form-control menuinput_multiline mainnav']")) # Use a more robust locator here (e.g., a specific XPath or ID if available)
    )
    texton.click()
    tkinter_text = text1.get("1.0", "end-1c")
    texton.send_keys(tkinter_text)
    texton.send_keys(Keys.RETURN)
    time.sleep(200)
    vi = driver.find_element(By.ID,"gametext")
    direct_text = driver.execute_script("""
        var text = '';
        var children = arguments[0].childNodes;
        for (var i = 0; i < children.length; i++) {
            if (children[i].nodeType === Node.TEXT_NODE) {
                text += children[i].nodeValue;
            }
        }
        return text.trim();
    """, vi)
    text2.insert(tk.END,direct_text+"\n")
    time.sleep(5)
    driver.close()
def ser():
    global direct
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get("https://chat.openai.com/")
    body = driver.find_element(By.TAG_NAME, "body")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Move the mouse to the body element, and then move by an offset to click
    # 10, 10 are the x and y coordinates relative to the top-left corner of the body
    actions.move_to_element_with_offset(body, 10, 10).send_keys(Keys.RETURN).perform()

        # Adjust selector based on current ChatGPT UI
    prompt_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "prompt-textarea"))
        )
    prompt_input.click()

    tkinter_text = text1.get("1.0", "end-1c")
    prompt_input.send_keys(tkinter_text)
    prompt_input.send_keys(Keys.RETURN)  # Simulate pressing Enter
    # --- Retrieve the response ---
    # Wait for the response to appear (adjust selector as needed)
    try:

        # 3. Wait for the p tag within the markdown div
        response = WebDriverWait(driver, 60).until(  # Use the markdown_div as the parent
            EC.presence_of_element_located((By.XPATH,"//div[@class='markdown prose dark:prose-invert w-full break-words light markdown-new-styling']")))

        latest_response = response.text
        direct= latest_response
        #else:
            #print("No response found.")
    except Exception as e:
        print(f"Could not retrieve response: {e}")

    # --- Clean up ---
    time.sleep(50)  # Keep browser open for a few seconds to observe
    driver.close()
def sreek():
    global value1
    if value1 == "chatgpt":
        selenium_thread = threading.Thread(target=ser)
        selenium_thread.start()
    if value1 == "others":
        selenium_thread1 = threading.Thread(target=serv)
        selenium_thread1.start()
def val2():
    global value1
    value1="others"
s=tk.Tk()
s.title("aiprompt")
pil_image = Image.open(f"{sreek1()}")
icon_image = ImageTk.PhotoImage(pil_image)
s.iconphoto(True, icon_image)
label1= tk.Label(s,text ="which ai do you want?")
label1.pack()
button1 = tk.Button(s,text="chatgpt",command=val1)
button1.pack()
button2 = tk.Button(s,text="qwen",command=val2)
button2.pack()
label=tk.Label(s,text="what do you want from ai?" )
label.pack()
text1 = tk.Text(s,background="black",height=8, width=50,fg="white")
text1.pack()
label1=tk.Label(s,text="response:")
label1.pack()
text2 = tk.Text(s,background="black", height=20, width=50,fg="white")
text2.pack()
button = tk.Button(s,text="submit", background="blue",command =sreek)
button.pack()
s.mainloop()







