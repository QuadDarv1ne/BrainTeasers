    #include <iostream>
    #include <string>
    #include <vector>
    #include <map>
    #include <limits>
    #include <memory>
    #include <locale>
    #include <cstdlib> // Для system()

    using namespace std;

    // Функция для очистки экрана
    void clearScreen() {
    #ifdef _WIN32
        system("cls"); // Для Windows
    #else
        system("clear"); // Для Linux/macOS
    #endif
    }

    // Перечисления
    enum class ProgrammerLevel { Junior, Middle, Senior };

    // Класс для задач
    class Task {
    public:
        string description;

        Task(const string& desc) : description(desc) {}

        void displayTask() const {
            cout << description << endl;
        }
    };

    // Базовый класс для всех сотрудников
    class Person {
    protected:
        string name, surname, patronymic;
        double salary;

    public:
        Person(const string& n, const string& s, const string& p, double sal)
            : name(n), surname(s), patronymic(p), salary(sal) {}

        virtual ~Person() = default;

        virtual void displayInfo() const {
            cout << "ФИО: " << surname << " " << name << " " << patronymic << ", Зарплата: " << salary << endl;
        }

        virtual void performDuties() = 0;

        virtual string getRole() const = 0;

        string getName() const { return name; }
        string getSurname() const { return surname; }
        string getPatronymic() const { return patronymic; }
        double getSalary() const { return salary; }
    };

    // Класс для бухгалтеров
    class Accountant : public Person {
    public:
        Accountant(const string& n, const string& s, const string& p, double sal)
            : Person(n, s, p, sal) {}

        void performDuties() override {
            cout << "Работа бухгалтера: расчеты выполнены.\n";
        }

        string getRole() const override {
            return "Бухгалтер";
        }

        void calculateSalary() {
            cout << "Зарплата бухгалтера: " << salary << " руб.\n";
        }

        void awardBonus() {
            salary += 1000;  // Премия
            cout << "Бухгалтеру выдана премия. Новая зарплата: " << salary << " руб.\n";
        }
    };

    // Класс для секретарей
    class Secretary : public Person {
    public:
        Secretary(const string& n, const string& s, const string& p, double sal)
            : Person(n, s, p, sal) {}

        void performDuties() override {
            cout << "Работа секретаря: задачи выполнены.\n";
        }

        string getRole() const override {
            return "Секретарь";
        }

        void organizeMeeting() {
            cout << "Секретарь организует встречу.\n";
        }
    };

    // Класс для программистов
    class Programmer : public Person {
        ProgrammerLevel level;
        vector<string> techStack;
        vector<Task> tasks;

    public:
        Programmer(const std::string& n, const std::string& s, const std::string& p, double sal, ProgrammerLevel lvl, const std::vector<std::string>& tech)
            : Person(n, s, p), salary(sal), level(lvl), techStack(tech) {}

        void displayTechStack() const {
            cout << "Навыки программиста: ";
            for (const auto& tech : techStack) cout << tech << " ";
            cout << endl;
        }

        string getLevelAsString() const {
            switch (level) {
                case ProgrammerLevel::Junior: return "Junior";
                case ProgrammerLevel::Middle: return "Middle";
                case ProgrammerLevel::Senior: return "Senior";
                default: return "Unknown";
            }
        }

        void performDuties() override {
            cout << "Работа программиста: код написан и протестирован.\n";
        }

        string getRole() const override {
            return "Программист";
        }

        void displayInfo() const override {
            Person::displayInfo();
            cout << "Уровень: " << getLevelAsString() << endl;
            displayTechStack();
            cout << "Список задач:\n";
            displayTasks();
        }

        // Методы для работы с задачами
        void addTask(const string& taskDesc) {
            tasks.push_back(Task(taskDesc));
            cout << "Задача добавлена.\n";
        }

        void deleteTask(int taskIndex) {
            if (taskIndex < 0 || taskIndex >= tasks.size()) {
                cout << "Некорректный индекс задачи.\n";
            } else {
                tasks.erase(tasks.begin() + taskIndex);
                cout << "Задача удалена.\n";
            }
        }

        void modifyTask(int taskIndex, const string& newDesc) {
            if (taskIndex < 0 || taskIndex >= tasks.size()) {
                cout << "Некорректный индекс задачи.\n";
            } else {
                tasks[taskIndex].description = newDesc;
                cout << "Задача изменена.\n";
            }
        }

        void displayTasks() const {
            if (tasks.empty()) {
                cout << "Нет задач.\n";
            } else {
                for (size_t i = 0; i < tasks.size(); ++i) {
                    cout << i + 1 << ". ";
                    tasks[i].displayTask();
                }
            }
        }
    };

    // Класс для директора
    class Director : public Person {
    public:
        Director(const string& n, const string& s, const string& p, double sal)
            : Person(n, s, p, sal) {}

        void performDuties() override {
            cout << "Работа директора: руководство компанией, принятие ключевых решений.\n";
        }

        string getRole() const override {
            return "Директор";
        }

        void manageCompany() {
            cout << "Директор управляет компанией и принимает решения.\n";
        }
    };

    // Класс для системного администратора
    class SystemAdministrator : public Person {
    public:
        SystemAdministrator(const string& n, const string& s, const string& p, double sal)
            : Person(n, s, p, sal) {}

        void performDuties() override {
            cout << "Работа системного администратора: поддержка и настройка IT инфраструктуры.\n";
        }

        string getRole() const override {
            return "Системный администратор";
        }

        void maintainSystems() {
            cout << "Системный администратор поддерживает серверы и сети.\n";
        }
    };

    // Класс для UX/UI дизайнера
    class UXUIDesigner : public Person {
    public:
        UXUIDesigner(const string& n, const string& s, const string& p, double sal)
            : Person(n, s, p, sal) {}

        void performDuties() override {
            cout << "Работа UX/UI дизайнера: проектирование пользовательского интерфейса.\n";
        }

        string getRole() const override {
            return "UX/UI дизайнер";
        }

        void createDesign() {
            cout << "UX/UI дизайнер создает дизайн интерфейсов.\n";
        }
    };

    // Менеджер для управления меню
    class MenuManager {
        vector<shared_ptr<Person>> employees;

    public:
        void addEmployee(const shared_ptr<Person>& employee) {
            employees.push_back(employee);
        }

        void displayMainMenu() {
            while (true) {
                clearScreen(); // Очистить экран перед показом меню
                cout << "\n--- Главное меню ---\n";
                for (size_t i = 0; i < employees.size(); ++i) {
                    cout << i + 1 << ". " << employees[i]->getRole() << ": "
                        << employees[i]->getSurname() << " " << employees[i]->getName() << " " << employees[i]->getPatronymic();

                    // Для программиста выводим только его уровень
                    if (auto programmer = dynamic_pointer_cast<Programmer>(employees[i])) {
                        cout << " (Уровень: " << programmer->getLevelAsString() << ")";
                    }

                    cout << endl;
                }
                cout << employees.size() + 1 << ". Выход\n";
                cout << "> ";

                int choice;
                cin >> choice;
                cin.ignore(numeric_limits<streamsize>::max(), '\n');

                if (choice == static_cast<int>(employees.size()) + 1) break;

                if (choice > 0 && choice <= static_cast<int>(employees.size())) {
                    displayEmployeeDetails(choice - 1);
                } else {
                    cout << "Неверный выбор. Попробуйте снова.\n";
                }
            }
        }

        void displayEmployeeDetails(int index) {
            while (true) {
                clearScreen(); // Очистить экран перед показом деталей сотрудника
                cout << "\n--- Детали сотрудника ---\n";
                employees[index]->displayInfo();
                employees[index]->performDuties();

                // В зависимости от типа сотрудника, предоставляем дополнительные функции
                if (auto programmer = dynamic_pointer_cast<Programmer>(employees[index])) {
                    cout << "\n--- Дополнительные функции программиста ---\n";
                    cout << "1. Добавить задачу\n";
                    cout << "2. Удалить задачу\n";
                    cout << "3. Изменить задачу\n";
                    cout << "4. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        string taskDesc;
                        cout << "Введите описание задачи: ";
                        getline(cin, taskDesc);
                        programmer->addTask(taskDesc);
                    } else if (action == 2) {
                        int taskIndex;
                        cout << "Введите номер задачи для удаления: ";
                        cin >> taskIndex;
                        programmer->deleteTask(taskIndex - 1);  // Индексы с 1
                    } else if (action == 3) {
                        int taskIndex;
                        string newDesc;
                        cout << "Введите номер задачи для изменения: ";
                        cin >> taskIndex;
                        cin.ignore();  // Чистим буфер
                        cout << "Введите новое описание задачи: ";
                        getline(cin, newDesc);
                        programmer->modifyTask(taskIndex - 1, newDesc);
                    } else if (action == 4) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                } else if (auto accountant = dynamic_pointer_cast<Accountant>(employees[index])) {
                    cout << "\n--- Дополнительные функции бухгалтера ---\n";
                    cout << "1. Рассчитать зарплату\n";
                    cout << "2. Выдать премию\n";
                    cout << "3. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        accountant->calculateSalary();
                    } else if (action == 2) {
                        accountant->awardBonus();
                    } else if (action == 3) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                } else if (auto secretary = dynamic_pointer_cast<Secretary>(employees[index])) {
                    cout << "\n--- Дополнительные функции секретаря ---\n";
                    cout << "1. Организовать встречу\n";
                    cout << "2. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        secretary->organizeMeeting();
                    } else if (action == 2) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                } else if (auto director = dynamic_pointer_cast<Director>(employees[index])) {
                    cout << "\n--- Дополнительные функции директора ---\n";
                    cout << "1. Управлять компанией\n";
                    cout << "2. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        director->manageCompany();
                    } else if (action == 2) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                } else if (auto sysAdmin = dynamic_pointer_cast<SystemAdministrator>(employees[index])) {
                    cout << "\n--- Дополнительные функции системного администратора ---\n";
                    cout << "1. Поддерживать системы\n";
                    cout << "2. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        sysAdmin->maintainSystems();
                    } else if (action == 2) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                } else if (auto designer = dynamic_pointer_cast<UXUIDesigner>(employees[index])) {
                    cout << "\n--- Дополнительные функции UX/UI дизайнера ---\n";
                    cout << "1. Создать дизайн\n";
                    cout << "2. Вернуться в главное меню\n";
                    cout << "> ";

                    int action;
                    cin >> action;
                    cin.ignore();

                    if (action == 1) {
                        designer->createDesign();
                    } else if (action == 2) {
                        break;
                    } else {
                        cout << "Неверный выбор.\n";
                    }
                }
            }
        }
    };

    int main() {
        MenuManager menuManager;

        // Добавляем сотрудников
        menuManager.addEmployee(make_shared<Accountant>("Анна", "Иванова", "Владимировна", 50000));
        menuManager.addEmployee(make_shared<Secretary>("Елена", "Петрова", "Сергеевна", 35000));
        menuManager.addEmployee(make_shared<Programmer>("Иван", "Смирнов", "Александрович", 80000, ProgrammerLevel::Senior, {"C++", "Python", "Java"}));
        menuManager.addEmployee(make_shared<Director>("Алексей", "Васильев", "Михайлович", 150000));
        menuManager.addEmployee(make_shared<SystemAdministrator>("Николай", "Голубев", "Игоревич", 60000));
        menuManager.addEmployee(make_shared<UXUIDesigner>("Марина", "Соколова", "Евгеньевна", 70000));

        menuManager.displayMainMenu();

        return 0;
    }
