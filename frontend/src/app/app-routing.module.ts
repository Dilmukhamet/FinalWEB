import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BooksComponent } from './books/books.component';
import { BookdetailComponent } from './bookdetail/bookdetail.component';
import { AddbookComponent } from './addbook/addbook.component';
const routes: Routes = [
  { path: "", redirectTo: "/books", pathMatch: "full"},
  { path: 'books/:id', component: BookdetailComponent },
  { path: "books", component: BooksComponent},
  { path: "createbook", component: AddbookComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
