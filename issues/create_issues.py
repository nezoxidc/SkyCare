"""
Создаёт задачи участников команды SkyCare в GitHub Issues (задание 5).

Как запустить (один раз, из любой папки):
  1. Установить GitHub CLI: https://cli.github.com  и выполнить  gh auth login
  2. Вписать GitHub-логины участников в словарь LOGINS ниже (пустая строка = без исполнителя).
  3. python create_issues.py
Скрипт создаст метки, задачи и файл ссылки_на_задачи.md со ссылками.
"""
import subprocess, sys, os, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tasks_data import PEOPLE, TASKS

REPO = 'nezoxidc/SkyCare'
LOGINS = {
    'bogodyuk': '', 'kanevsky': '', 'ivankov': '', 'mashkin': '',
    'artemyev': '', 'pavlov': '', 'chentemirov': '',
}
LABELS = {'analytics': '7B61FF', 'management': '0E8A16', 'devops': '1D76DB', 'docs': 'C5DEF5',
          'architecture': '5319E7', 'backend': 'D93F0B', 'frontend': 'FBCA04', 'testing': 'B60205'}


def gh(*args):
    r = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print('Ошибка:', r.stderr.strip())
    return r.stdout.strip()


for name, color in LABELS.items():
    gh('label', 'create', name, '--repo', REPO, '--color', color, '--force')

links = []
for t in TASKS:
    person, role = PEOPLE[t['who']]
    body = (f"**Исполнитель:** {person} ({role})\n**Срок:** {t['due']}\n\n"
            f"### Зачем\n{t['why']}\n\n### Что сделать\n" + '\n'.join(f'- {x}' for x in t['do']) +
            "\n\n### Критерии успеха\n" + '\n'.join(f'- [ ] {x}' for x in t['done']))
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(body); path = f.name
    args = ['issue', 'create', '--repo', REPO, '--title', t['title'], '--body-file', path, '--label', t['label']]
    if LOGINS.get(t['who']):
        args += ['--assignee', LOGINS[t['who']]]
    url = gh(*args)
    os.unlink(path)
    print(url, '-', t['title'])
    links.append(f"- {person}: [{t['title']}]({url}) — срок {t['due']}")

with open('ссылки_на_задачи.md', 'w', encoding='utf-8') as f:
    f.write('# Задачи участников SkyCare\n\n' + '\n'.join(links) + '\n')
print('Готово, ссылки записаны в ссылки_на_задачи.md')
