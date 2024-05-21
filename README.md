1. Install via pip 
``` pip install crewai_logger_patch```
2. Add import into your main crewai file - This needs to be above any other crewai imports
``` import crewai_logger_patch```
3. Add the patch method to your code - This needs to be above any otehr crewai imports
```apply_monkey_patch()```
4. Add the following below your agent instances - You msut use your agent names in place of <placeholder_name>
```<placeholder_name>._logger = crewai.utilities.Logger(verbose_level=<placeholder_name>.verbose)```
5. And the same below your crew instance
