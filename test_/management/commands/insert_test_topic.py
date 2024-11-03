from django.core.management.base import BaseCommand
from test_.models import TestTopic

class Command(BaseCommand):
    help = 'Insert predefined test topics into the TestTopic table'

    def handle(self, *args, **kwargs):
        # Define the topics and their corresponding batch IDs
        topics = [
            ("Java Basics", 1),
            ("Java OOP Concepts", 1),
            ("Java Collections", 1),
            ("Java Threads", 1),
            ("Java Streams", 1),
            ("Java I/O", 1),
            ("Java Exceptions", 1),
            ("Java Network Programming", 1),
            ("Java Concurrency", 1),
            ("Java Swing", 1),
            ("Java FX", 1),
            ("Java Servlets", 1),
            ("Java JSP", 1),
            ("Java Spring Framework", 1),
            ("Java Hibernate", 1),
            ("Java Security", 1),
            ("Java Memory Management", 1),
            ("Java Lambda Expressions", 1),
            ("Java Functional Interfaces", 1),
            ("Java Multithreading", 1),
            ("Java Annotations", 1),
            ("Java Reflection", 1),
            ("Java Generics", 1),
            ("Java Sockets", 1),
            ("Java Design Patterns", 1),
            ("ASP.NET Basics", 2),
            ("ASP.NET Core", 2),
            ("C# Basics", 2),
            ("ASP.NET MVC", 2),
            ("Entity Framework", 2),
            ("ASP.NET Collections", 2),
            ("LINQ", 2),
            ("ASP.NET Exceptions", 2),
            ("ASP.NET Multithreading", 2),
            ("ASP.NET Delegates", 2),
            ("ASP.NET Web API", 2),
            ("Windows Forms", 2),
            ("WPF", 2),
            ("Xamarin", 2),
            ("Blazor", 2),
            ("ASP.NET Security", 2),
            ("Azure Basics", 2),
            ("SignalR", 2),
            ("ASP.NET Routing", 2),
            ("ASP.NET Razor", 2),
            ("WCF", 2),
            ("Data Engineering Basics", 3),
            ("Python for Data Engineering", 3),
            ("SQL Basics", 3),
            ("ETL Processes", 3),
            ("Data Warehousing", 3),
            ("Big Data Concepts", 3),
            ("Data Lakes", 3),
            ("Apache Hadoop", 3),
            ("Apache Spark", 3),
            ("Data Pipelines", 3),
            ("Airflow", 3),
            ("Kafka Basics", 3),
            ("Data Modeling", 3),
            ("Data Cleaning", 3),
            ("NoSQL Databases", 3),
            ("Relational Databases", 3),
            ("Cloud Data Engineering", 3),
            ("AWS for Data Engineering", 3),
            ("Data Streaming", 3),
            ("Data Governance", 3),
            ("Data Security", 3),
            ("Data Partitioning", 3),
            ("Data Versioning", 3),
            ("Data Lakehouse", 3),
            ("Data Engineering with Spark", 3),
        ]

        # Insert each topic into the TestTopic table
        for topic_name, batch_id in topics:
            TestTopic.objects.create(topic_name=topic_name, batch_id=batch_id)

        self.stdout.write(self.style.SUCCESS('Successfully inserted topics into the TestTopic table.'))