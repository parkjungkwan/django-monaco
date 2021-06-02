from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Name', 'Sex', 'Cabin', 'Ticket', 'Fare')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1. Train 의 type \n {type(this.train)} ')
        print(f'2. Train 의 column \n {this.train.columns} ')
        print(f'3. Train 의 상위 1개 행\n {this.train.head()} ')
        print(f'4. Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5. Test 의 type \n {type(this.test)}')
        print(f'6. Test 의 column \n {this.test.columns}')
        print(f'7. Test 의 상위 1개 행\n {this.test.head()}개')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)


