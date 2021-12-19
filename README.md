### RT-RW APP

#### 1. Complete setup

		E:.
		├───apps
		│   ├───core
		│   │   ├───migrations
		│   │   │   └───__pycache__
		│   │   └───__pycache__
		│   ├───desa
		│   │   ├───migrations
		│   │   │   └───__pycache__
		│   │   └───__pycache__
		│   ├───rt09
		│   │   ├───migrations
		│   │   │   └───__pycache__
		│   │   └───__pycache__
		│   ├───rt12
		│   │   ├───migrations
		│   │   │   └───__pycache__
		│   │   └───__pycache__
		│   └───rw14
		│       ├───migrations
		│       │   └───__pycache__
		│       └───__pycache__
		└───config
		    └───__pycache__


#### 2. Complete up to desa, rw14, rt09 and rt12

		NOTE:

		1. Desa can do CRUD for desa and view all
		2. Rw can do CRUD for rw and view all
		3. Rt09 can do CRUD for rt09 and wargart09
		4. Rt12 can do CRUD for rt12 and wargart12


#### 3. Create more apps and add more functionalities

        modified:   README.md
        modified:   apps/core/models.py
        modified:   apps/desa/admin.py
        new file:   apps/desa/migrations/0001_initial.py
        modified:   apps/desa/models.py
        new file:   apps/rt01/__init__.py
        new file:   apps/rt01/admin.py
        new file:   apps/rt01/apps.py
        new file:   apps/rt01/migrations/0001_initial.py
        new file:   apps/rt01/migrations/__init__.py
        new file:   apps/rt01/models.py
        new file:   apps/rt01/tests.py
        new file:   apps/rt01/views.py
        new file:   apps/rt02/__init__.py
        new file:   apps/rt02/admin.py
        new file:   apps/rt02/apps.py
        new file:   apps/rt02/migrations/0001_initial.py
        new file:   apps/rt02/migrations/__init__.py
        new file:   apps/rt02/models.py
        new file:   apps/rt02/tests.py
        new file:   apps/rt02/views.py
        new file:   apps/rt03/__init__.py
        new file:   apps/rt03/admin.py
        new file:   apps/rt03/apps.py
        new file:   apps/rt03/migrations/0001_initial.py
        new file:   apps/rt03/migrations/__init__.py
        new file:   apps/rt03/models.py
        new file:   apps/rt03/tests.py
        new file:   apps/rt03/views.py
        new file:   apps/rt04/__init__.py
        new file:   apps/rt04/admin.py
        new file:   apps/rt04/apps.py
        new file:   apps/rt04/migrations/0001_initial.py
        new file:   apps/rt04/migrations/__init__.py
        new file:   apps/rt04/models.py
        new file:   apps/rt04/tests.py
        new file:   apps/rt04/views.py
        new file:   apps/rt05/__init__.py
        new file:   apps/rt05/admin.py
        new file:   apps/rt05/apps.py
        new file:   apps/rt05/migrations/0001_initial.py
        new file:   apps/rt05/migrations/__init__.py
        new file:   apps/rt05/models.py
        new file:   apps/rt05/tests.py
        new file:   apps/rt05/views.py
        new file:   apps/rt06/__init__.py
        new file:   apps/rt06/admin.py
        new file:   apps/rt06/apps.py
        new file:   apps/rt06/migrations/0001_initial.py
        new file:   apps/rt06/migrations/__init__.py
        new file:   apps/rt06/models.py
        new file:   apps/rt06/tests.py
        new file:   apps/rt06/views.py
        new file:   apps/rt07/__init__.py
        new file:   apps/rt07/admin.py
        new file:   apps/rt07/apps.py
        new file:   apps/rt07/migrations/0001_initial.py
        new file:   apps/rt07/migrations/__init__.py
        new file:   apps/rt07/models.py
        new file:   apps/rt07/tests.py
        new file:   apps/rt07/views.py
        new file:   apps/rt08/__init__.py
        new file:   apps/rt08/admin.py
        new file:   apps/rt08/apps.py
        new file:   apps/rt08/migrations/0001_initial.py
        new file:   apps/rt08/migrations/__init__.py
        new file:   apps/rt08/models.py
        new file:   apps/rt08/tests.py
        new file:   apps/rt08/views.py
        modified:   apps/rt09/admin.py
        new file:   apps/rt09/migrations/0001_initial.py
        modified:   apps/rt09/models.py
        new file:   apps/rt10/__init__.py
        new file:   apps/rt10/admin.py
        new file:   apps/rt10/apps.py
        new file:   apps/rt10/migrations/0001_initial.py
        new file:   apps/rt10/migrations/__init__.py
        new file:   apps/rt10/models.py
        new file:   apps/rt10/tests.py
        new file:   apps/rt10/views.py
        new file:   apps/rt11/__init__.py
        new file:   apps/rt11/admin.py
        new file:   apps/rt11/apps.py
        new file:   apps/rt11/migrations/0001_initial.py
        new file:   apps/rt11/migrations/__init__.py
        new file:   apps/rt11/models.py
        new file:   apps/rt11/tests.py
        new file:   apps/rt11/views.py
        modified:   apps/rt12/admin.py
        new file:   apps/rt12/migrations/0001_initial.py
        modified:   apps/rt12/models.py
        modified:   apps/rw14/admin.py
        new file:   apps/rw14/migrations/0001_initial.py
        modified:   apps/rw14/models.py
        modified:   config/settings.py