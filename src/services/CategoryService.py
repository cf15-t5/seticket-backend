
from src.repositories.CategoryRepository import CategoryRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service
from src.utils.validator.CategoryValidator import CreateNewCategoryValidator,UpdateCategoryValidator,DeleteCategoryValidator

from src.utils.errorHandler import errorHandler
categoryRepository = CategoryRepository()    

class CategoryService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
    def getAllCategories(self):
        try:
            data = categoryRepository.getAllCategories()
            return CategoryService.failedOrSuccessRequest('success', 200, queryResultToDict(data))
        except Exception as e:
            return CategoryService.failedOrSuccessRequest('failed', 500, str(e))
    
    def createCategory(self,data):
        try:
            validate = CreateNewCategoryValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            newCategory = categoryRepository.createNewCategory(data)
            return self.failedOrSuccessRequest('success', 201, queryResultToDict([newCategory])[0])
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return self.failedOrSuccessRequest('failed', 500, str(e))
          
    def updateCategory(self,id,data):
        try:
          validate = UpdateCategoryValidator(**data,id=id)
          if not validate:
              return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
          event = categoryRepository.getCategoryById(id)
          if not event:
            return self.failedOrSuccessRequest('failed', 404, 'Category not found')
          categoryUpdated = categoryRepository.updateCategory(id,data)
          return self.failedOrSuccessRequest('success', 201, queryResultToDict([categoryUpdated])[0])
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return self.failedOrSuccessRequest('failed', 500, str(e))
          
    def deleteCategory(self,id):
        try:
          validate = DeleteCategoryValidator(id=id)
          if(not validate):
            return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
          event = categoryRepository.getCategoryById(id)
          if not event:
            return self.failedOrSuccessRequest('failed', 404, 'Event not found')
          
          categoryRepository.deleteCategory(id)
          return self.failedOrSuccessRequest('success', 200, 'Event deleted')
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return self.failedOrSuccessRequest('failed', 500, str(e))