import sys
import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        percent = (i / total) * 100
        bar_length = 50
        filled_length = int(bar_length * i // total)
        bar = "=" * filled_length
        
        sys.stdout.write(f"\r{percent:.0f}%|[{bar}>]| {i}/{total} [{elapsed_time:.2f}s, {speed:.2f}it/s]")
        sys.stdout.flush()
        
        yield item
    
    print()
