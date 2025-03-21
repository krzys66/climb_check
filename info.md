# Dokumentacja projektu

## Potencjalne zastosowania projektu

Projekt może znaleźć zastosowanie w różnych dziedzinach, takich jak:
- **Bezpieczeństwo w sportach ekstremalnych**: Monitorowanie wspinaczy w czasie rzeczywistym, aby upewnić się, że są odpowiednio zabezpieczeni.
- **Szkolenia i edukacja**: Analiza materiałów wideo w celu szkolenia wspinaczy i instruktorów.
- **Automatyzacja nadzoru**: Wykorzystanie systemu w halach wspinaczkowych lub na zewnętrznych trasach wspinaczkowych do automatycznego wykrywania potencjalnych zagrożeń.

## Wykonanie programu

1. **Model detekcji obiektów**  
   W projekcie wykorzystano model YOLO, a dokładnie wersję `yolo11m`. Model został wytrenowany na podstawie 150 zdjęć, co pozwoliło na osiągnięcie odpowiedniej skuteczności w detekcji obiektów.

2. **Użyte biblioteki**  
   W programie zastosowano następujące biblioteki:
   - `openCV` – do przetwarzania obrazu,
   - `ultralytics` – do obsługi modelu YOLO,
   - `numpy` – do operacji na danych numerycznych.

3. **Proces trenowania modelu**  
   Do trenowania modelu wykorzystano gotowy kod. Proces trenowania został przeprowadzony na platformie Google Colab, co umożliwiło użycie GPU i przyspieszyło obliczenia.

4. **Działanie programu**  
   - Program sprawdza, czy dane źródło (np. wideo) ma jeszcze klatki do przetworzenia.
   - Dla każdej klatki analizuje, czy znajduje się na niej jeden z dwóch obiektów:
     - człowiek z liną,
     - człowiek bez liny.
   - Jeśli program wykryje człowieka bez liny, wyświetlane jest ostrzeżenie.
   - Ostrzeżenie pojawia się tylko wtedy, gdy model ma co najmniej 70% pewności, że człowiek nie ma liny. Ten próg można edytować w kodzie lub ustawić przy uruchamianiu programu.

## Rzeczy do zmiany

1. **Poprawa wyświetlania obrazu**  
   Obecnie filmik (w prezentacji) jest przyspieszony 4-krotnie, co powoduje, że w rzeczywistości klatki są wyświetlane bardzo wolno. Należy zoptymalizować wyświetlanie obrazu, aby działało płynniej.

2. **Rozszerzenie zbioru danych**  
   Aby poprawić skuteczność modelu, warto stworzyć większy zbiór danych treningowych. Powinien on zawierać zdjęcia różnych osób, wykonane z różnych perspektyw i przy użyciu różnych kamer.

3. **Projektowanie UI**  
   - Należy zaprojektować bardziej estetyczny interfejs użytkownika.
   - Poprawić sposób wyświetlania ostrzeżeń, aby były bardziej czytelne i atrakcyjne wizualnie.

4. **Testowanie z kamerą**  
   Program należy przetestować, korzystając z kamerki, aby upewnić się, że działa poprawnie w czasie rzeczywistym.

## Jak uruchomić program

1. Otwórz Anaconda Prompt i wpisz następujące komendy:
   ```
   conda create -n "env_name"
   conda activate your_env
   ```

2. Przejdź do folderu, w którym znajduje się plik modelu:
   ```
   cd path/to/folder (Folder zawierający plik my_model.pt)
   ```

3. Upewnij się, że biblioteka ultralytics jest zainstalowana w utworzonym środowisku:
   ```
   pip install ultralytics
   ```

4. Uruchom skrypt z odpowiednimi parametrami:
   ```
   python your_script.py --model path_to_model.pt --source path_to_video.jpg --window_size 640x480
   ```

   W tym przypadku:
   - `your_script.py` to np. `climbcheck.py`,
   - `path_to_model.pt` to np. `my_model/my_model.pt`,
   - `path_to_video.jpg` to ścieżka do wideo (może to być również kamera USB).

5. Opcjonalnie możesz dodać parametr `--thresh`, który pozwala ustawić próg pewności detekcji (domyślny próg to 0.7).

