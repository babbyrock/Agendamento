import { environment } from '../../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, ReplaySubject } from 'rxjs';
import { User } from '../models/User';
import { take, map } from 'rxjs/operators';

@Injectable()
export class AccountService {

  private currentUserSource = new ReplaySubject<User>(1);
  currentUser$ = this.currentUserSource.asObservable();

  baseUrl = environment.apiURL + ''

  constructor(private http: HttpClient) { }

  public login(model: any): Observable<void>{
    return this.http.post<User>(this.baseUrl + 'login/', model).pipe(
      take(1),
      map((response: User) =>{
        const user = response;
        if (user){
          this.setCurrentUser(user)
        }
      })
    );
  }

  public register(model: any): Observable<void>{
    return this.http.post<User>(this.baseUrl + 'cadastrar_usuario/', model).pipe(
      take(1),
      map((response: User) =>{
        const user = response;
        if (user){
          this.setRegisterCurrentUser(user)
        }
      })
    );
  }


  logout(): void {
    localStorage.removeItem('user');
    this.currentUserSource.next(null as any);
    this.currentUserSource.complete();
  }

  public setCurrentUser(user: User): void{
    localStorage.setItem('user', JSON.stringify(user));
    this.currentUserSource.next(user);
  }

  public setRegisterCurrentUser(user: User): void{
    localStorage.setItem('register-user', JSON.stringify(user));
    this.currentUserSource.next(user);
  }
}
