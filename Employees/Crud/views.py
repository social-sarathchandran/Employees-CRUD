from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from .utils import CustomPagination, APIResponse


# Employee CRUD operations
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Viewsets for handling CURD operations of Employee objects

    Attributes:
        1.querysets(Queryset):The request of employee objects
        2.serializer_class(Serializer): The serializer class for employee objects
        3.pagination_class(Pagination) : The pagination class for paginating results

    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        """
        Method for creating a new employee object

        Returns:
            1. Response: A response message with appropriate success or error message
        """

        try:
            response = super().create(request, *args, **kwargs)
            return APIResponse(
                "Employee created successfully", data=response.data
            ).build_response()
        except Exception as e:
            return APIResponse(error=str(e)).build_response()

    def update(self, request, *args, **kwargs):
        """
        Method for updating an existing employee object

        Returns:
            1. Response: A response message with appropriate success or error message
        """

        try:
            response = super().update(request, *args, **kwargs)
            return APIResponse(
                "Employee updated successfully", response.data
            ).build_response()
        except Exception as e:
            return APIResponse(error=str(e)).build_response()

    def destroy(self, request, *args, **kwargs):
        """
        Method for deleting an existing employee object

        Returns:
            1. Response: A response message with appropriate success or error message
        """
        try:
            response = super().destroy(request, *args, **kwargs)
            return APIResponse(
                "Employee deleted successfully", response.data
            ).build_response()
        except Exception as e:
            return APIResponse(error=str(e)).build_response()
