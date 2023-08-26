from src.models.Category import Category,db

class CategoryRepository:
  def getAllCategories(self):
    return Category.query.all()  
  
  def createNewCategory(self,data):
    newCategory = Category(name=data['name'])
    db.session.add(newCategory)
    db.session.commit()
    return newCategory
  
  def getCategoryById(self,category_id):
    return Category.query.filter_by(category_id=category_id).first()
  
  def updateCategory(self,id,data):
    category = Category.query.filter_by(category_id=id).first()
    if(not category) :return False
    category.name = data['name']
    db.session.commit()
    return category
  
  def deleteCategory(self,id):
    category = Category.query.filter_by(category_id=id).first()
    if(not category) :return False
    db.session.delete(category)
    db.session.commit()
    return True
  def getCategoryByName(self,name):
    return Category.query.filter_by(name=name).first()