:: SHA 256 Everything in a specific folder
for %f in (*.*) do certutil -hashfile "%f" SHA256
