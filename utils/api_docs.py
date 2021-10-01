def docs(file_path: str) -> str:
    with open(file_path, mode='r') as f:
        return f.read() 

