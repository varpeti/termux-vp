# termux-vp

A termux appomat tartom szinkronban a gépemmel ezen a repon keresztül.

## Scriptek:

### symlinkall:

#### Fileok:

- symlinkall.py
    - Szinkronizálja a cfg alapján a widgettel és taskerrel a scripteket.
- symlinkall.cfg
    -filename widget tasker
    -melyik **filename**et szinkronizálja a **widget**el és/vagy a tasker**rel
    - 0 - nem , 1 - igen

---

### randomWallpaper

#### Fileok, mappák:

- randomWallpaper-get.sh
    - letölt 20 random háttérképet a **dataRandomWallpaper/out** mappába
- randomWallpaper-set.py
    - beállít egy random képet a letöltött képek közül
- randomWallpaper-del.py
    - törli az aktuális háttérképet és beálít egy másikat
- dataRandomWallpaper
    - out 
        - letöltött képek
    - cur.cfg
        - az aktuális háttérkép neve

---

### battery

#### Fileok:

- battery.sh
    - Kiírja a battery státuszát.

---